from utils import *
from sklearn import linear_model

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
