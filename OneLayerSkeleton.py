import numpy as np
import matplotlib as plt
import matplotlib.image as mpimg

# NN with 1 hidden layer of n nodes skeleton for binary classification:
def layer_sizes(X, Y):
    return n_x, n_h, n_y # where h is the single hidden layer
def initialize_parameters(n_x, n_h, n_y):
    return parameters # where parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2}
def forward_propagation(X, parameters):
    return A2, cache # where cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}
def compute_cost(A2, Y):
    return cost
def backward_propagation(parameters, cache, X, Y):
    return grads # where grads = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}
def update_parameters(parameters, grads, learning_rate=0.01):
    return parameters
def nn_model(X, Y, n_h, num_iterations=10000):
    return parameters
def predict(parameters, X):
    return predictions # where predictions spans the same demensions as Y | post gradient descent
# example execution:
parameters = nn_model(X, Y, n_h=4, num_iterations=10000)
predict(parameters, x.T)