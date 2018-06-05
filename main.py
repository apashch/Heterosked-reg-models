from utils import *
from GLSE import *
from NONLIN import *
import matplotlib.pyplot as plt


if __name__ == "__main__":
	df = getdata()
	o = dict()
	for dset in range(1, 6):
		o[dset] = [LSE(df[dset]), GLSEI(df[dset]), GLSEII(df[dset]), WLSE(df[dset]), LASSO(df[dset]), Ridge(df[dset]), Huber(df[dset])]
	
	#get R2 values in a table
	for k in o.keys():
		#print(k)
		for m in range(len(o[1])):
			print(model_evaluation(o[k][m])[0], end = ',')
		print(' ')

	#get RMSE values in a table
	for k in o.keys():
		#print(k)
		for m in range(len(o[1])):
			print(model_evaluation(o[k][m])[2], end = ',')
		print(' ')

			


	for k in o.keys():
		fig, ax = plt.subplots(figsize=(18, 12))
		ax.scatter(df[k].x, df[k].y)
		ax.plot(df[k].x, o[k][0][-2], color = 'b', label = 'LSE')
		ax.plot(df[k].x, o[k][1][0] + o[k][1][1]*df[k].x, color = 'r', label = 'GLSEI')
		ax.plot(df[k].x, o[k][2][0] + o[k][2][1]*df[k].x, color = 'g', label = 'GLSEII')
		ax.plot(df[k].x, o[k][3][0] + o[k][3][1]*df[k].x, color = 'm', label = 'WLSE')
		legend = ax.legend()
		plt.savefig("pred_plot_{}_upd".format(k))
		plt.close()

	# for k in o.keys():
	# 	fig, ax = plt.subplots(figsize=(18, 12))
	# 	ax.scatter(df[k].x, get_residuals2(df[k].x, o[k][1]))
	# 	plt.savefig("GLSE_residuals_{}".format(k))
	# 	plt.close()

