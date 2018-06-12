from utils import *
from sklearn import linear_model

# This file contains regressionss with non-linear loss functions (LASSO, Ridge) and Huber's regression 

# output of each model is a an array of following values
# a1 : y-intersception estimate
# a2 : slope estimate
# yhat : vector of  predicted Y  values
# y : vector of true Y values copied from input

def LASSO(data):
	X = data.drop("y", axis = 1)
	y = data["y"]
	lr = linear_model.LassoCV(eps = 0.0001, n_alphas = 1000)
	lr.fit(X, y)
	a1, a2 = lr.intercept_, lr.coef_[1]
	return(a1, a2, lr.predict(X), y)

def Ridge(data):
	X = data.drop("y", axis = 1)
	y = data["y"]
	lr = linear_model.RidgeCV(alphas = np.arange(-20, 20, 0.05), )
	lr.fit(X, y)
	a1, a2 = lr.intercept_, lr.coef_[1]
	return(a1, a2, lr.predict(X), y)

def Huber(data, epsilon = 1.6):
	X = data.drop("y", axis = 1)
	y = data["y"]
	lr = linear_model.HuberRegressor()
	lr.fit(X, y)
	a1, a2 = lr.intercept_, lr.coef_[1]
	return(a1, a2, lr.predict(X), y)
