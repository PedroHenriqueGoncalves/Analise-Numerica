# Bibliotecas
import numpy as np
import math

# Declarando os parametros
a = 1
b = 2
tol = 1e-04 # Erro de tolerância
erro = 2*tol # Erro inicial para erro ser maior que a tolerância
x0 = 1.8
x1 = 1.7
iter = 0
iter_max = 0

# Definindo a função
def G(x):
  return (math.exp(x) - 2*x - 1)

# Método da Secante
while (erro > tol):
  x = x0 - G(x0) * ((x1 - x0) / (G(x1) - G(x0)))
  erro = abs(x-x1)/(abs(x)) # Erro Relativo
  x0 = np.copy(x1)
  x1 = np.copy(x)
  iter += 1
  print("iter", iter , ", x = ", x)

print("\n Número de Iterações: ", iter)
