from utils import *
from GLSE import *
from LASSO import *


if __name__ == "__main__":
	df = getdata()
	o = dict()
	for dset in range(1, 6):
		#print(heteroskedacity_test(df[dset]))
		o[dset] = LSE(df[dset]), GLSE(df[dset]), LASSO(df[dset]), Ridge(df[dset]), Huber(df[dset]), WLSE(df[dset])
	for k in o.keys():
		print(heteroskedacity_test(df[k]))
		print(model_evaluation(o[k][0]))
		print(model_evaluation(o[k][1]))
		print(model_evaluation(o[k][2]))
		print(model_evaluation(o[k][3]))
		print(model_evaluation(o[k][4]))
		print(model_evaluation(o[k][5]))

