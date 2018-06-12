from sklearn import linear_model, metrics
from utils import *

# This file contains functions with linear loss functions -  LSE, WLSE andtwo versions of GLSE

# output of each model is  a an array of following values
# a1 : y-intersception estimate
# a2 : slope estimate
# yhat : vector of  predicted Y  values
# y : vector of true Y values copied from input

def LSE(data):
	X = data.drop("y", axis = 1)
	y = data["y"]
	lr = linear_model.LinearRegression()
	lr.fit(X, y)
	if len(lr.coef_) > 2:
		a1, a2, a3 = lr.intercept_, lr.coef_[1], lr.coef_[2]
		return (a1, a2, a3, lr.predict(X), y)
	else:
		a1, a2 = lr.intercept_, lr.coef_[1]
		return [a1, a2, lr.predict(X), y]

def WLSE(data):
	homdata = data.multiply(data.x.abs().pow(-0.5), axis = 0)
	return LSE(homdata)[:-1] + [data.y]

#difference between GLSEI and GLSEII is described in the report
def GLSEI(data, error_dist = lambda x: np.log(abs(x))):
	res2 = get_residuals(data)**2
	aux_data = pd.DataFrame(data = {'y': np.log(res2), 'z': error_dist(data.x), 'const': [1]*len(data.x)})
	a1, a2, yhat, y = LSE(aux_data)
	sigmahat2 = np.exp(aux_data.z*a2 + a1)
	homdata = data.multiply(sigmahat2.pow(-0.5), axis = 0)
	#print("GLSEI coefficents:", a1, a2)
	return LSE(homdata)[:-1] + [data.y]

def GLSEII(data):
	res2 = get_residuals(data)**2
	aux_data = pd.DataFrame(data = {'y': res2,'x': data.x,'const': [1]*len(data.x)})
	a1, a2, yhat, y = LSE(aux_data)
	sigmahat2 = aux_data.x.abs()*a2 + a1
	sigmahat2[sigmahat2 < 0] = 1
	homdata = data.multiply(sigmahat2.pow(-0.5), axis = 0)
	#print("GLSEII coefficents:", a1, a2)
	return LSE(homdata)[:-1] + [data.y]


