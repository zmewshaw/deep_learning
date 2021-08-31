import idx2numpy
import numpy as np
imageFile = "C:/Users/zmews/GitHub/machine-learning/mnist/train-images.idx3-ubyte"
labelFile = "C:/Users/zmews/GitHub/machine-learning/mnist/train-labels.idx1-ubyte"
imageArr = idx2numpy.convert_from_file(imageFile)
labelArr = idx2numpy.convert_from_file(labelFile)