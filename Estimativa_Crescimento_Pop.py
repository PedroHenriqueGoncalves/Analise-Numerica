import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('populacao_crescimento_presidente_prudente.dat', sep='\t', na_values=['NA'])
print(df.head())

plt.scatter(df['Ano'], df['Pop'])
plt.xlabel('Ano')
plt.ylabel('População')
plt.title('Estimativa do crescimento populacional de Presidente Prudente')
plt.show()

b = (len(df) * sum(df['Ano'] * df['Pop']) - sum(df['Ano']) * sum(df['Pop'])) / (len(df) * sum(df['Ano'] ** 2) - (sum(df['Ano'])) ** 2)
a = (sum(df['Pop']) - b * sum(df['Ano'])) / len(df)
print("Temos quer os parâmetros parra a e b:")
print(f'a = {a}')
print(f'b = {b}')

y = b*df['Ano'] + a

# Estimativas para os anos de 2025 e 2030
y_2025 = b*2025 + a
y_2030 = b*2030 + a

print('Estimativas para os anos de 2025 e 2030:')
print(f'2025: {y_2025:.2f}')
print(f'2030: {y_2030:.2f}')

plt.plot(df['Ano'], y)
plt.scatter(df['Ano'], df['Pop'])
plt.xlabel('Ano')
plt.ylabel('População')
plt.title('Estimativa do crescimento populacional de Presidente Prudente')
plt.legend(['Regressão Linear', 'Dados'])
plt.show()