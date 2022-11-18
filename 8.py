from math import factorial

x=[0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25]
y=[ 4.4817,4.9530,5.4739,6.0496,6.6859,7.3891,8.1662,9.0250,9.9742,11.0232,12.1825] 
h = x[1] - x[0]
x1=0.159
x2=0.173
q=(x1 - x[0])/h
q1 = (x2-x[-1])/h
def n(y,j): #обчислення кінцевих різниць 
   mas=[]
   for i in range(len(y)): 
      mas.append(y[i] - y[i-1])
   mas.pop(0) 
   if j == 1:
      return mas 
   else:
      j-=1
      return n(mas, j)
s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)
n_1 = s_1 + s_2 + s_3 + s_4
print ('The value of a function at a point x1=', x1, 'using Newton*s First Interpolation Formula', round(n_1,5))

s_1 = y[5]+q1*n(y,1)[4]+q1*(q1+1)*n(y,2)[3]/factorial(2)
s_2 = q1*(q1+1)*(q1+2)*n(y,3)[2]/factorial(3)
s_3 = q1*(q1+1)*(q1+2)*(q1+3)*n(y,4)[1]/factorial(4)
s_4 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*n(y,5)[0]/factorial(5) 
n_1 = s_1 + s_2 + s_3 + s_4
print ('The value of a function at a point x1=', x2, 'using Newton*s Second Interpolation Formula', round(n_1,5))


