from sklearn import linear_model, metrics
from utils import *

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

def GLSE(data, error_dist = lambda x: np.log(abs(x))):
	res2 = get_residuals(data)**2
	aux_data = pd.DataFrame(data = {'y': np.log(res2), 'z': error_dist(data.x), 'const': [1]*len(data.x)})
	a1, a2, yhat, y = LSE(aux_data)
	sigmahat2 = np.exp(aux_data.z*a2 + a1)
	homdata = data.multiply(sigmahat2.pow(-1), axis = 0)
	print("GLSE coefficents:", a1, a2)
	return LSE(homdata)[:-1] + [data.y]

def WLSE_sq(data):
	res2 = get_residuals(data)**2
	aux_data = pd.DataFrame(data = {'y': res2,'x': data.x,'x2': data.x.pow(2),'const': [1]*len(data.x)})
	a1, a2, a3, yhat, y = LSE(aux_data)
	#print(a1, a2, a3)
	sigmahat2 = aux_data.x2.pow(2)*a3+aux_data.x*a2 + a1
	homdata = data.multiply(sigmahat2.pow(-1), axis = 0)
	return LSE(homdata)[:-1] + [data.y]

def WLSE_lin(data):
	res2 = get_residuals(data)**2
	aux_data = pd.DataFrame(data = {'y': res2,'x': data.x,'const': [1]*len(data.x)})
	a1, a2, yhat, y = LSE(aux_data)
	#print(a1, a2)
	sigmahat2 = aux_data.x*a2 + a1
	homdata = data.multiply(sigmahat2.pow(-1), axis = 0)
	return LSE(homdata)[:-1] + [data.y]


