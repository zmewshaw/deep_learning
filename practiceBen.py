import numpy as np

def main():
    x = np.random.randn(2, 10)
    w = np.random.randn(2, 1)
    b = np.zeros((1, 1))
    z = np.dot(w.T, x) + b
    print("z: " + str(z))
main()