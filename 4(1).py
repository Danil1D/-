import numpy as np
A = np.matrix('1 1 1; 0 1 1; 0 0 1')
print(A)
B = np.matrix('7 5 3; 0 7 5; 0 0 7')
print(B)
C = A.dot(B)
D = B.dot(A)
F = C-D
print(F)
