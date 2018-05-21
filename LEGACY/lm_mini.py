import numpy as np
from sklearn import linear_model


x = (1, 2, 3)
y = (1, 2, 4)

lm = linear_model.LinearRegression()
lm.fit(x,y)

