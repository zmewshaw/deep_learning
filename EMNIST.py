import idx2numpy
import numpy as np
import matplotlib as plt

train_images = "C:/Users/zmews/GitHub/Datasets/mnist/train-images.idx3-ubyte"
train_labels = "C:/Users/zmews/GitHub/Datasets/mnist/train-labels.idx1-ubyte"
test_images = "C:/Users/zmews/GitHub/Datasets/mnist/t10k-images.idx3-ubyte"
test_labels = "C:/Users/zmews/GitHub/Datasets/mnist/t10k-labels.idx1-ubyte"

X_train_orig = idx2numpy.convert_from_file(train_images)
Y_train = idx2numpy.convert_from_file(train_labels)
X_test_orig = idx2numpy.convert_from_file(test_images)
Y_test = idx2numpy.convert_from_file(test_labels)

# alter (flatten) training and test set if necessary (global) - x.reshape(x.shape[0], -1).T - gives a vector
# standardize dataset if necessary

def initializeParametersDeep(layerDims):
    return parameters
def lModelForward(X, parameters):
    return AL, caches
def computeCost(AL, Y):
    return cost
def lModelBackward(AL, Y, caches):
    return grads
def updateParameters(parameters, grads, learningRate):
    return parameters
# implement with a function: xLayers(X, Y, layerDims, learningRate = x, numIterations = x, printCost = False)