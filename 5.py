import matplotlib.pyplot as plt
from scipy import optimize
import math
x0 = 0.15
y0 = -2.1
delta = 0.1
def f1(y):
   return (-1+math.sin(y))/2
def f2 (x):
   return math.cos(x+0.5)-2
def iter (x,y,e):
   xn = x
   yn = y
   xn1 = f2(x)
   yn1 = f1(y)
   n = 1
   while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):
       xn = xn1
       yn = yn1
       xn1 = f2(yn)
       yn1 = f1(xn)
       n += 1
   print ('Simple iteration:')
   print ('x=', xn, '\ny=',yn,'\nThe amount of iteration = ',n)
iter(x0,y0,0.001)

plt.axis([0, 5, -5, 0])
plt.xlabel('x')
plt.ylabel('y')
fig, ax = plt.subplots()
xs = []
ys = []
sin_vals = []
cos_vals = []
x = -5
y = -5
while x < 5.0:
    sin_vals += [ -2+math.cos( x +0.5) ]
    cos_vals += [ -1/2+1/2 * math.sin(y) ]
    xs += [x]
    ys += [x]
    x += 0.1
    y += 0.1
ax.vlines(0,-5, 5)
ax.hlines(0, -5,5)
plt.plot(xs, sin_vals, color = 'blue', linestyle = 'solid')
plt.plot(cos_vals,ys,  color = 'red', linestyle = 'solid')

plt.show()
