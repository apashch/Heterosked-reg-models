from utils import *
from GLSE import *
from LASSO import *
import matplotlib.pyplot as plt


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

	for k in o.keys():
		fig, ax = plt.subplots()
		ax.scatter(df[k].x, df[k].y)
		ax.plot(df[k].x, o[k][0][-2], color = 'b', label = 'LSE')
		#ax.scatter(df[k].x, o[k][1][-2], color = 'r', label = 'GLSE')
		ax.plot(df[k].x, o[k][1][0] + o[k][1][1]*df[k].x, color = 'r', label = 'GLSE')
		legend = ax.legend()
		plt.savefig("pred_plot_{}_2".format(k))
		plt.close()

