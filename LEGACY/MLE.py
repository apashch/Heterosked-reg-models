from utils import *
from scipy.optimize import minimize

def beta(x, u, n = -1):
	if n >= 0:
		res = np.exp(np.dot(u, x[n]))
		return res
	else:
		return np.exp(np.dot(u, x))
def y(x, w, n = -1):
	if n >= 0:
		return np.dot(w, x[n])
	else:
		return np.dot(w, x)
def en(t, n, x, w):
	res = 0.5*np.power((y(x, w, n)-t[n]), 2)
	return res


def S(w, *args):
	t, x, u = args
	alpha = 0.1
	res = alpha/2 * np.linalg.norm(w)**2
	for i in list(range(t.size)):
		res += np.inner(beta(x = x, u = u, n = i), en(t, i, x, w))
	return res

def A(t, x, u):
	alpha = 0.1
	res = alpha
	for i in list(range(t.size)):
		print(np.inner(beta(x = x, u = u, n = i), x[i]**2))
		res += np.inner(beta(x = x, u = u, n = i), x[i]**2)
	print("In A", res.shape)
	return res

def M(u, *args):
	t, x, w = args
	alpha = 0.1
	res = np.log(A(t, x, u))*0.5 + alpha/2 * np.linalg.norm(u)**2
	print(res.size)
	for i in list(range(t.size)):
		res += np.inner(beta(x = x, u = u, n = i), en(t, i, x, w)) - 0.5*np.log(beta(x = x, u = u, n = i))

def opt_w(u):
	global t, x, w
	w = minimize(S, w, args = (t, x, u)).x
	print(w.size)


def MLE(data):
	t = data.y
	x = data.x
	u = np.array([1, 1])
	w = np.array([1, 1])
	u = minimize(M, u, args = (t, x, w), callback = opt_w).x
	print(u)






