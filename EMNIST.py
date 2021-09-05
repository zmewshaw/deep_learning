import idx2numpy
import numpy as np

trainImages = "C:/Users/zmews/GitHub/deep-learning/mnist/train-images.idx3-ubyte"
trainLabels = "C:/Users/zmews/GitHub/deep-learning/mnist/train-labels.idx1-ubyte"
testImages = "C:/Users/zmews/GitHub/deep-learning/mnist/t10k-images.idx3-ubyte"
testLabels = "C:/Users/zmews/GitHub/deep-learning/mnist/t10k-labels.idx1-ubyte"

trainImageArr = idx2numpy.convert_from_file(trainImages)
trainLabelArr = idx2numpy.convert_from_file(trainLabels)
testSetX = idx2numpy.convert_from_file(testImages)
testLabelArr = idx2numpy.convert_from_file(testLabels)