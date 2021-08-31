import idx2numpy
import numpy as np
import tensorflow as tf
from tensorflow import keras

testImages = "C:/Users/Zach/GitHub/machine-learning/mnist/t10k-images.idx3-ubyte"
testLabels = "C:/Users/Zach/GitHub/machine-learning/mnist/t10k-labels.idx1-ubyte"
trainImages = "C:/Users/Zach/GitHub/machine-learning/mnist/train-images.idx3-ubyte"
trainLabels = "C:/Users/Zach/GitHub/machine-learning/mnist/train-labels.idx1-ubyte"

testImageArr = idx2numpy.convert_from_file(testImages)
testLabelArr = idx2numpy.convert_from_file(testLabels)
trainImageArr = idx2numpy.convert_from_file(trainImages)
trainLabelArr = idx2numpy.convert_from_file(trainLabels)
