from utils import *
from MLE import *

if __name__ == "__main__":
	abc = np.array([1,2]).reshape(1, 2)
	c = [4]
	print(np.dot(abc.transpose(), c))

	df = getdata()
	o = dict()
	#for dset in range(1, 6):
	for dset in range(1, 2):
		o = MLE(df[dset])
		print(o)
