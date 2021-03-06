import numpy as np
from scipy.optimize import fsolve

def func(X):
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    L = X[3]
    G = X[4]
    return x1*x2*x3 + L * (2*x1*x2 + x2*x3 - 12) + G * (2*x1 - x2 - 8)

def dfunc(X):
    dLambda = np.zeros(len(X))
    h = 1e-3 
    for i in range(len(X)):
        dX = np.zeros(len(X))
        dX[i] = h
        dLambda[i] = (func(X+dX)-func(X-dX))/(2*h)
    return dLambda


X1 = fsolve(dfunc, [1, 1, -6, 0, 0])
print (f"max: {X1}, {func(X1)}")

X1 = fsolve(dfunc, [-1, -1, -1, 0, 0])
print (f"min: {X1}, {func(X1)}")



