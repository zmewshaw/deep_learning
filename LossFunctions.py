import numpy as np
import matplotlib.pyplot as plt

# hyperparams
learningRate = 0.01
n = 2

for i in range(n):
    

# MSE functions
def MSE():
    return yMSE, dxMSE, "MSE"
def yMSE(x):
    return x ** 2
def dxMSE(x):
    return x * 2

# MAE functions
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
def main():
    x1 = np.random.randn(n, 1) * 100
    x2 = np.copy(x1)

    w1 = np.random.randn(n, 1)
    w2 = np.copy(w1)
    print(w1)

    print(calcLoss(MSE, x1))
    print(calcLoss(MAE, x2))
main()