import numpy as np
A = np.matrix('1 2 0 0 0; 1 0 2 0 0; 1 0 0 2 0; 1 0 0 0 2; 0 0 1 1 1')
print(A)
A_det = np.linalg.det(A) 
print(format(A_det, '.9g'))
