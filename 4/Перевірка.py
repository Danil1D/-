import numpy as np
a = np.matrix('1 -2 3; 4 2 -3; 3 -3 5')
b = np.matrix('-5; 0; -9')
X = np.linalg.solve(a, b)
print('Перевірка X=',X)
