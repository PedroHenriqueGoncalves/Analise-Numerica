import numpy as np
import math
import matplotlib.pyplot as plt
def f(x,y):
  return(y-(x**2) +1)

def EulerAperfeicoado(a,b,y0,N):
  h=(b-a)/N
  y = np.zeros(N+1)
  x = np.zeros(N+1)
  z = np.zeros(N+1)
  y[0] = y0
  for i in range(N+1):
    x[i] = a + i*h
    z[i] = (x[i] + 1)**2 - 0.5*math.exp(x[i])
  y[1] = y[0] + h*f(x[0],y[0])
  for i in range(N):
    k1 = f(x[i],y[i])
    k2 = f(x[i+1], y[i] + h*k1)
    y[i+1] = y[i] + (h/2)*(k1 + k2)
  return x,y,z

a=0
b=0.5
N=10
y0=0.5

x,y,z = EulerAperfeicoado(a,b,y0,N)
plt.scatter(x,y,label="aprox.")
erro = np.linalg.norm(z - y)
print(erro)
plt.plot(x,z,label="exato")
plt.legend()
plt.show()


