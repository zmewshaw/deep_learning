import idx2numpy
import numpy as np
import matplotlib as plt

trainImages = "C:/Users/zmews/GitHub/deep-learning/mnist/train-images.idx3-ubyte"
trainLabels = "C:/Users/zmews/GitHub/deep-learning/mnist/train-labels.idx1-ubyte"
testImages = "C:/Users/zmews/GitHub/deep-learning/mnist/t10k-images.idx3-ubyte"
testLabels = "C:/Users/zmews/GitHub/deep-learning/mnist/t10k-labels.idx1-ubyte"

trainSetXOrig = idx2numpy.convert_from_file(trainImages)
trainSetY = idx2numpy.convert_from_file(trainLabels)
testSetXOrig = idx2numpy.convert_from_file(testImages)
testSetY = idx2numpy.convert_from_file(testLabels)

A = np.array([[1], [2], [3], [4]])
B = np.array(1, 2, 3)
print("A: " + str(A))
print("B: " + str(B))
print("np.dot(A, B): " + str(np.dot(A, B)))

# steps:
# alter training and test set if needed (global) - x.reshape(x.shape[0], -1).T - gives a vector
def initializeParameters(n_x, n_h, n_y):
    return parameters
def linearActivationForward(A_prev, W, b, activation):
    return A, cache
def computeCost(AL, Y):
    return cost
def linearActivationBackward(dA, cache, activation):
    return dA_prev, dW, db
def updateParameters(parameters, grads, learningRate):
    return parameters