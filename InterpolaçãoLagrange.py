import numpy as np
import matplotlib.pyplot as plt

# Função original
def f(x):
    return 1 / (1 + x**2)

# Função de interpolação de Lagrange (genérica)
def interpolacao(x, y, xi):
    n = len(x)
    S = 0
    for k in range(n):
        L = 1
        for i in range(n):
            if i != k:
                L *= (xi - x[i]) / (x[k] - x[i])
        S += y[k] * L
    return S

# Parâmetros
a, b = -5, 5

n_values = [2, 6, 8]

# Ponto de interesse
x_ponto = 4.3
# Valor interpolado
f_real = f(x_ponto)

# Gráficos
for n in n_values:
    x = np.linspace(a, b, n+1)
    y = f(x)

    # Ponto e valores interpolados
    x_plot = np.linspace(a, b, 400)
    Pn = np.array([interpolacao(x, y, xi) for xi in x_plot])
    # Solução exata
    y_exata = f(x_plot)

    # Gráficos
    plt.plot(x_plot, Pn, label=f'P{n}(x) (n={n})')
    plt.scatter(x, y, s=30)
    plt.plot(x_plot, y_exata, 'k--', label='f(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title(f'Interpolação de Lagrange para n = {n}')
    plt.show()
    print('')

print(80*'=')
print("Estimação do Erro para os três polinômios construídos no ponto x = 4.3")
print(80*'=')

for n in n_values:
    x = np.linspace(a, b, n + 1)
    y = f(x)
    Pn_x = interpolacao(x, y, x_ponto)
    #calculo do Erro
    erro = abs(f_real - Pn_x)
    erro_rel = abs((f_real - Pn_x) / f_real)
    print(f"n = {n} | f(4.3) = {f_real:.6f} | Pn(4.3) = {Pn_x:.6f} | Erro = {erro:.6f} | Erro Relativo = {erro_rel}")
