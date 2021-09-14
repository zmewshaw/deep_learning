import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize hyperparameters and variables | n is number of inputs, m is size of training set.
learning_rate = 0.01
n = 1
m = 100

X0 = np.random.randn(n, m)
Y0 = np.zeros((1, m))
W0 = np.random.randn(1, n)
b0 = np.zeros((1, 1))
dW0 = np.zeros((1, n))
db0 = np.zeros((1, 1))

def forward_prop(X, W, b):
    Z = np.dot(W, X) + b
    A = max(0, Z)
    MSE_X = np.sum(A ** 2) / m
    MAE_X = np.sum(abs(A)) / m
    Log_X = np.sum(-np.log(1 - A)) / m
    return Z, A, MSE_X, MAE_X, Log_X
# ALL FUNCTIONS ARE CENTERED AROUND 0 FOR SIMPLICITY (Y = 0), Y is not our actual Y axis, it is simply our labeled training set (zeros).
# MSE (Mean Squared Error) functions
# MAE (Mean Absolute Error) functions

# Get the position of all balls on the screen for animation
def get_pos(t=0):
    X, Y = X0, Y0
    parameters = W0, b0
    while True:
        cache = forward_prop(X, parameters)
        

# Initialize the figure for animation
def init():