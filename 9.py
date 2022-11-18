import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline 
import numpy as np
 
x = [0.7,0.8,1.3,1.5,2.1]
y = [2.63,2.87,2.19,1.76,3.34]

spl = UnivariateSpline(x, y) #Побудова сплайна
xs = np.linspace(0.7, 2.1, 1000) 
plt.plot(x,y,'ro', xs,spl(xs), 'g')
plt.show()

