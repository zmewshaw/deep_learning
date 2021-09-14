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

# alter training and test set if needed (global) - x.reshape(x.shape[0], -1).T - gives a vector
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