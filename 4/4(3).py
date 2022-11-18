import numpy as np
A = np.matrix('5 0 2 3; 4 1 5 3; 3 1 -1 2')
print(A)
B = np.matrix('6 ; -2 ; 7 ; 4')
print(B)
C = A.dot(B)
print(C)
