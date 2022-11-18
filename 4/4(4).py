import numpy as np
A = np.matrix('2 3 4; 1 0 6; 7 8 9')
print(A)
A_det = np.linalg.det(A) 
print(format(A_det, '.9g'))

