from utils import *
from GLSE import *
from NONLIN import *
import matplotlib.pyplot as plt

# **************************
# to operate with the dictionary o, use the follwing conventions
# o[k][i][j] - get j-th entry of the model i for the dataset k. 

# Ordering of models is as follows (consisent with the order in  metric tables in the report):
# 0 : Least Sqares Regression
# 1 : Generalized Least Sqares Regression w/assumed error variance ~ ax^b (GLSEI)
# 2 : Generalized Least Sqares Regression w/assumed error variance ~ cx + d (GLSEII)
# 3 : Weighted Least Sqares Regression 
# 4 : LASSO
# 5 : Ridge Regression
# 6 : Huner regression 

# Order of entries in model outputs are described in corresponding model-specification files (see GLSE.py and NONLIN.py)
# **************************


if __name__ == "__main__":
	# load data and perform model fitting
	df = getdata()
	o = dict()
	for dset in range(1, 6):
		o[dset] = [LSE(df[dset]), GLSEI(df[dset]), GLSEII(df[dset]), WLSE(df[dset]), LASSO(df[dset]), Ridge(df[dset]), Huber(df[dset])]
	

	#get R2 values in a table
	print("R2 Table")
	for k in o.keys():
		for m in range(len(o[1])):
			print(model_evaluation(o[k][m])[0], end = '|')
		print(' ')
	print('\n')

	#get RMSE values in a table
	print("RMSE table")
	for k in o.keys():
		for m in range(len(o[1])):
			print(model_evaluation(o[k][m])[2], end = '|')
		print(' ')

			
	#save parameter vectors for selected models
	with open("parameter-estimations.csv", 'w') as f:
		f.write("dataset, OLSE (a ; b),  GLSE (a ; b)\n")
		for k in o.keys():
			f.write(str(k) +  ',')
			f.write(str(o[k][0][0]) + "; " + str(o[k][0][1]) + ',')
			f.write(str(o[k][2][0]) + "; " + str(o[k][2][1]) + '\n')

	# plot the fitted lines for selected models 
	for k in o.keys():
	 	fig, ax = plt.subplots(figsize=(18, 12))
	 	ax.scatter(df[k].x, df[k].y)
	 	ax.plot(df[k].x, o[k][0][-2], color = 'b', label = 'LSE')
	 	ax.plot(df[k].x, o[k][1][0] + o[k][1][1]*df[k].x, color = 'r', label = 'GLSEI')
	 	ax.plot(df[k].x, o[k][2][0] + o[k][2][1]*df[k].x, color = 'g', label = 'GLSEII')
	 	ax.plot(df[k].x, o[k][3][0] + o[k][3][1]*df[k].x, color = 'm', label = 'WLSE')
	 	legend = ax.legend()
	 	plt.xlabel("X")
	 	plt.ylabel("Y")
	 	plt.title("Predictions of selected models on dataset {}".format(k), fontsize=20)

	 	plt.savefig("pred_plot_{}_upd".format(k))
	 	plt.close()

	#plot the residuals
	# for k in o.keys():
	# 	fig, ax = plt.subplots(figsize=(18, 12))
	# 	ax.scatter(df[k].x, get_residuals2(df[k].x, o[k][1]))
	# 	plt.savefig("GLSE_residuals_{}".format(k))
	# 	plt.close()

