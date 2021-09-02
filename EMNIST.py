import idx2numpy
import numpy as np

testImages = "C:/Users/zmews/GitHub/machine-learning/mnist/t10k-images.idx3-ubyte"
testLabels = "C:/Users/zmews/GitHub/machine-learning/mnist/t10k-labels.idx1-ubyte"
trainImages = "C:/Users/zmews/GitHub/machine-learning/mnist/train-images.idx3-ubyte"
trainLabels = "C:/Users/zmews/GitHub/machine-learning/mnist/train-labels.idx1-ubyte"

testImageArr = idx2numpy.convert_from_file(testImages)
testLabelArr = idx2numpy.convert_from_file(testLabels)
trainImageArr = idx2numpy.convert_from_file(trainImages)
trainLabelArr = idx2numpy.convert_from_file(trainLabels)

J = 0