import time
import numpy as np
import matplotlib.pyplot as plt

learningRate = 0.01
numRuns = 1000

def MSE(x):
    return x ** 2
def dMSE(x):
    return x * 2
def MAE(x):
    return abs(x)
def calcLoss(yFunc, dyFunc, s):
    x = np.random.randn(numRuns, 100)
    y = yFunc(x)
    dy = dyFunc(x)
    start = time.time()
    while not (-0.001 < dy < 0.001):
        dy = dyFunc(x)
        x -= learningRate * dy
        y = yFunc(x)
    end = time.time()
    totalTime = end - start
    return "{s} took {t} seconds to perform {n} calculations".format(s = s, t = totalTime, n = numRuns)
def main():
    print(calcLoss(MSE, dMSE, "MSE"))
    print(calcLoss())
main()