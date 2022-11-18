import numpy as np
A = np.matrix('-2 3 1 -1; 3 2 1 4; 1 2 3 4; 0 2 3 3')
print(A)
rank = np.linalg.matrix_rank(A)
print(rank)
