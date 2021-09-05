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

# steps:
# find m_train, m_test, num_px (global)
# flatten the training and test set (global)
# standardize the data set (global)
# sigmoid (function)
# initialize with 0s (function)
# propagate (function)
# optimize (function)
# predict (function)
# model (function)
# logisticRegressionModel = model(trainSetX, trainSetY, testSetX, testSetY, numIterations=TBD, learningRate=TBD)