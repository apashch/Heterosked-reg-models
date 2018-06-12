import pandas as pd
import numpy as np
from glob import glob
from sklearn import linear_model, metrics
from statsmodels.stats.diagnostic import het_white
from math import sqrt

# This file contains miscalenious functions that help with implementing and evaluating all models



# load data
def getdata(masterfolder = './'):
	filenames = glob(masterfolder+"data*.csv")
	data = dict()
	for fname in filenames:
		df = pd.read_csv(fname)
		df['const'] = 1
		# to be consistent, we want constant as the first column
		df = df.reindex(columns=sorted(df.columns))
		data[int(fname.split('_')[-1].split('.')[0])] = df
	return data

# implementing White Hetereroskedacity Test
def heteroskedacity_test(data, rejection_alpha = 0.05):
	res = get_residuals(data)
	het_test_results = het_white(resid = res, exog = data.drop('y', axis = 1))
	# comparing p-value to alpha
	return het_test_results[-1] < rejection_alpha

def root_mean_squared_error(y_true, y_pred):
	if len(y_true) != len(y_pred):
		return -1
	return sqrt(metrics.mean_squared_error(y_true, y_pred))

#get residuals from raw data
def get_residuals(data):
	X, y = data.drop("y", axis = 1), data["y"]
	lr = linear_model.LinearRegression()
	lr.fit(X, y)
	res = lr.predict(X) - y
	return res

#get residuals from the model output
def get_residuals2(x, model):
	y_true = model[-1]
	return  get_model_prediction(x, model[0], model[1]) - y_true

#use metrics on the estimation of a model
def model_evaluation(model_output):
	inter, slope, y_pred, y_true = model_output
	r2 = metrics.r2_score(y_true, y_pred)
	mse = metrics.mean_squared_error(y_true, y_pred)
	rmse = root_mean_squared_error(y_true, y_pred)
	return(r2, mse, rmse)

def get_model_prediction(x, a0, a1):
	return a0+a1*x


