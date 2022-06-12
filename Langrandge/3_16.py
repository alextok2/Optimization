import numpy as np
from scipy.optimize import fsolve

def func(X):
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    L = X[3] # 1 множитель
    G = X[4] # 2 множитель
    return x1 * x2 + x2 * x3 + L * (x1 + x2 - 4) + G * (x2 + x3 - 4)

def dfunc(X):
    dLambda = np.zeros(len(X))
    h = 1e-3 # размер шага
    for i in range(len(X)):
        dX = np.zeros(len(X))
        dX[i] = h
        dLambda[i] = (func(X+dX)-func(X-dX))/(2*h);
    return dLambda

X1 = fsolve(dfunc, [1, 1, 1, 0, 0])
print (X1, func(X1))

X2 = fsolve(dfunc, [-1, -1, -1, 0, 0])
print (X2, func(X2))


