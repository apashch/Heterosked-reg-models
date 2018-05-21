import pandas as pd
import numpy as np
from glob import glob
from sklearn import linear_model, metrics
from statsmodels.stats.diagnostic import het_white
from GLSE import *


def getdata(masterfolder = './'):
	filenames = glob(masterfolder+"*.csv")
	data = dict()
	for fname in filenames:
		df = pd.read_csv(fname)
		df['const'] = 1
		# to be consistent want constant as the first column
		df = df.reindex(columns=sorted(df.columns))
		data[int(fname.split('_')[-1].split('.')[0])] = df
	return data

# implementing White Hetereroskedacity Test
def heteroskedacity_test(data, rejection_alpha = 0.05):
	res = get_residuals(data)
	het_test_results = het_white(resid = res, exog = data.drop('y', axis = 1))
	# comparing p-value to alpha
	return het_test_results[-1] < rejection_alpha

def get_residuals(data):
	X, y = data.drop("y", axis = 1), data["y"]
	lr = linear_model.LinearRegression()
	lr.fit(X, y)
	res = lr.predict(X) - y
	return res

def model_evaluation(model_output):
	inter, slope, y_true, y_pred = model_output
	r2 = metrics.r2_score(y_true, y_pred)
	return(r2)


if __name__ == "__main__":
	df = getdata()
	o = dict()
	for dset in range(1, 6):
		#print(heteroskedacity_test(df[dset]))
		o[dset] = LSE(df[dset]), GLSE(df[dset])
	for k in o.keys():
		print(heteroskedacity_test(df[k]))
		print(model_evaluation(o[k][0]))
		print(model_evaluation(o[k][1]))


