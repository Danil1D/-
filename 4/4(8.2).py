import numpy as np
A = np.matrix('1 -2 3; 4 2 -3; 3 -3 5')
B = np.matrix('-5; 0; -9')
print ('A=',A)
print ('B=',B)
A_inv = np.linalg.inv(A)
print(A_inv)
x = A_inv.dot(B)
print('X=',x)
