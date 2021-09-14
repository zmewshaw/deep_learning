import numpy as np
import matplotlib as plt
import matplotlib.image as mpimg

train_images = "C:/Users/zmews/GitHub/deep-learning/Datasets/PerImages"
train_labels = "C:/Users/zmews/GitHub/deep-learning/mnist/train-labels.idx1-ubyte"
test_images = "C:/Users/zmews/GitHub/deep-learning/mnist/t10k-images.idx3-ubyte"
test_labels = "C:/Users/zmews/GitHub/deep-learning/mnist/t10k-labels.idx1-ubyte"

# Example of a picture
img = mpimg.imread("")

def sigmoid(z):
    # INSERT CODE HERE
    return s

def initialize_with_zeros(dim):
    # INSERT CODE HERE
    return w, b

def propagate(w, b, X, Y):
    # INSERT CODE HERE
    return grads, cost # where grads = {"dw": dw, "db": db} | grads stands for gradients

def optimize(w, b, X, Y, num_iterations=100, learning_rate=0.01):
    # INSERT CODE HERE
    return params, grads, costs # where params = {"w": w, "b": b}

def predict(w, b, X):
    # INSERT CODE HERE
    return Y_prediction # where Y_prediction spans the same dimensions as Y | post gradient descent

def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.01):
    # INSERT CODE HERE
    return d # where d = {"costs":costs, "Y_prediction_test":Y_prediction_test,  "Y_prediction_train":Y_prediction_train,  "w":w,  "b":b, "learning_rate":learning_rate, "num_iterations":num_iterations}

# example execution:
logistic_regression_model = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations=2000, learning_rate=0.001)