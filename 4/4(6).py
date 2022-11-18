import numpy as np
A = np.matrix('2 1 0 0; 3 2 0 0;1 1 3 4; 2 -1 2 3')
print(A)
A_inv = np.linalg.inv(A)
print(A_inv)

