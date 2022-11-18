from scipy.misc import derivative

def f(x):
  return 6*x**4 + 4*x**3 - x**2 - x - 10

def hord (a, b, eps): 
    if abs(f(b) - f(a)) < eps:
      print('Нема корнів')
      return
    if (f(a) * derivative(f, a, n=2)):
      x0 = a
      xi = b
    else:
      x0 = b
      xi = a
    xi_1 = xi-(xi-x0) * f(xi) / f((xi) - f(x0))
    while (abs(f(xi_1) - f(xi)) > eps):
      xi = xi_1
      xi_1 = xi-(xi - x0) * f(xi) / (f(xi) - f(x0))
    else:
        print(f'Корінь знаходиться в точці x = ', xi_1)

hord(1, 2, 0.0001)
