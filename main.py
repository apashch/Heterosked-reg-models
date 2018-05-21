from utils import *
from GLSE import *


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

