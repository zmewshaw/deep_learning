import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize hyperparameters and variables | n is number of inputs, m is size of training set.
learningRate = 0.01
n = 2
m = 100

X = np.random.randn(n, m)

W = np.random.randn(1, n)
b = np.zeros((n, 1))

# ALL FUNCTIONS ARE CENTERED AROUND 0 FOR SIMPLICITY (Y = 0)
# MSE (Mean Squared Error) functions
def MSE():
    return yMSE, dxMSE, "MSE"
def yMSE(x):
    return x ** 2
def dxMSE(x):
    return x * 2

# MAE (Mean Absolute Error) functions
def MAE():
    return yMAE, dxMAE, "MAE"
def yMAE(x):
    return abs(x)
def dxMAE(x):
    return x / abs(x)

# LOG functions
def log():
    return yLog, dxLog, "Log"
def yLog(x):
    return -1
def dxLog(x):
    return -1

# Loss calculation
def calcLoss(funcs, x):
    yFunc, dxFunc, funcName = funcs()
    dx = dxFunc(x)
    xGraph = []
    yGraph = []
    steps = 0
    while not ((np.sum(x) < 0.001) and (np.sum(x) > -0.001)):
        xGraph.append(x)
        dx = dxFunc(x)
        x -= learningRate * dx
        steps += 1
    return xGraph, yGraph

print(calcLoss(MSE, x1))
print(calcLoss(MAE, x2))