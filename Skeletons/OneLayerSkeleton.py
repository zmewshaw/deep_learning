import numpy as np
import matplotlib as plt

train_images = "C:/Users/zmews/GitHub/"
train_labels = "C:/Users/zmews/GitHub/"
test_images = "C:/Users/zmews/GitHub/"
test_labels = "C:/Users/zmews/GitHub/"

# Dataset - TBD (binary classification)

# NN with 1 hidden layer of n nodes skeleton for binary classification:
def layer_sizes(X, Y):
    # INSERT CODE HERE
    return n_x, n_h, n_y # where h is the single hidden layer

def initialize_parameters(n_x, n_h, n_y):
    # INSERT CODE HERE
    return parameters # where parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2}

def forward_propagation(X, parameters):
    # INSERT CODE HERE
    return A2, cache # where cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}

def compute_cost(A2, Y):
    # INSERT CODE HERE
    return cost

def backward_propagation(parameters, cache, X, Y):
    # INSERT CODE HERE
    return grads # where grads = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}

def update_parameters(parameters, grads, learning_rate=0.01):
    # INSERT CODE HERE
    return parameters

def nn_model(X, Y, n_h, num_iterations=10000):
    # INSERT CODE HERE
    return parameters

def predict(parameters, X):
    # INSERT CODE HERE
    return predictions # where predictions spans the same demensions as Y | post gradient descent

# example execution:
parameters = nn_model(X, Y, n_h=4, num_iterations=10000)
# predict(parameters, X) allows you to model the data