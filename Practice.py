import numpy as np

D1 = np.random.rand(3, 3)
print(D1)
D1 = (D1 > .5).astype(int)
print(D1)
A1 = np.random.randn(3, 3)
print(A1)
A1 *= D1
print(A1)