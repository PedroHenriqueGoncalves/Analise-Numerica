import numpy as np
import matplotlib.pyplot as plt
import math

# Função do PVI
def f(x, y):
    return 5*y - 1   # corrigido conforme o enunciado

# Solução exata (usada para o erro e o gráfico)
def y_exata(x):
    return math.exp(5*x) + 0.2

# ================================
# Métodos Numéricos
# ================================

def EulerExplicito(a, b, N, y0):
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    z = np.zeros(N+1)
    h = (b - a)/N
    for i in range(N+1):
        x[i] = a + i*h
        z[i] = y_exata(x[i])
    y[0] = y0
    for i in range(N):
        y[i+1] = y[i] + h*f(x[i], y[i])
    return x, y, z

def EulerImplicito(a, b, N, y0):
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    z = np.zeros(N+1)
    h = (b - a)/N
    for i in range(N+1):
        x[i] = a + i*h
        z[i] = y_exata(x[i])
    y[0] = y0
    for i in range(N):
        y[i+1] = (y[i] - h) / (1 - 5*h)
    return x, y, z

def Trapezio(a, b, N, y0):
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    z = np.zeros(N+1)
    h = (b - a)/N
    for i in range(N+1):
        x[i] = a + i*h
        z[i] = y_exata(x[i])
    y[0] = y0
    for i in range(N):
        y[i+1] = ((1 + (5*h/2))*y[i] - (h/2)) / (1 - (5*h/2))
    return x, y, z

def PontoMedio(a, b, N, y0):
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    z = np.zeros(N+1)
    h = (b - a)/N
    for i in range(N+1):
        x[i] = a + i*h
        z[i] = y_exata(x[i])
    y[0] = y0
    for i in range(N):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + (h/2)*k1)
        y[i+1] = y[i] + h*k2
    return x, y, z

# ================================
# Função genérica para o erro
# ================================

def calcula_erro(y_aprox, y_exato):
    erro = np.abs(y_aprox - y_exato)
    erro_max = np.max(erro)
    return erro, erro_max

# ================================
# Parâmetros e execução
# ================================

a = 0
b = 2
y0 = 1.2
N = 20

# Métodos
xe, ye, ze = EulerExplicito(a, b, N, y0)
xi, yi, zi = EulerImplicito(a, b, N, y0)
xt, yt, zt = Trapezio(a, b, N, y0)
xp, yp, zp = PontoMedio(a, b, N, y0)

# Cálculo genérico do erro
erro_e, erro_max_e = calcula_erro(ye, ze)
erro_i, erro_max_i = calcula_erro(yi, zi)
erro_t, erro_max_t = calcula_erro(yt, zt)
erro_p, erro_max_p = calcula_erro(yp, zp)

# Impressão dos erros máximos
print(f"Erro máximo Euler Explícito: {erro_max_e:.5e}")
print(f"Erro máximo Euler Implícito: {erro_max_i:.5e}")
print(f"Erro máximo Trapézio:        {erro_max_t:.5e}")
print(f"Erro máximo Ponto Médio:     {erro_max_p:.5e}")

# ================================
# Gráfico comparativo
# ================================
plt.plot(xe, ze, 'k-', label='Solução Exata')
plt.scatter(xe, ye, color='red', label='Euler Explícito')
plt.scatter(xi, yi, color='blue', label='Euler Implícito')
plt.scatter(xt, yt, color='green', label='Trapézio')
plt.scatter(xp, yp, color='orange', label='Ponto Médio')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid()
plt.title('Comparação dos Métodos Numéricos e Erros')
plt.show()
