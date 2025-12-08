import numpy as np

#Sistema Triangular Superior
def SistemaTriangularSuperior(A,b):
  n=len(b)
  x=np.zeros(n)
  x[n-1] = b[n-1]/A[n-1][n-1]
  for i in range(1,n):
    ind = (n-1)-i
    soma=0
    for k in range(ind+1,n):
      soma=soma + A[ind][k]*x[k]
    x[ind] = (b[ind] - soma)/A[ind][ind]

  return x
#Sistema Triangular Inferior
def SistemaTriangularInferior(A,b):
  n=len(b)
  x=np.zeros(n)
  x[0]=b[0]/A[0][0];
  for i in range(1,n):
    soma=0
    for k in range(i):
      soma = soma + A[i][k]*x[k]
    x[i] = (b[i] - soma)/A[i][i]
  return x


#Decomposição LU
def DecomposicaoLU(A):

  n=A.shape[0]

  U = np.zeros((n,n))#matriz de zeros
  L = np.eye(n)#identidade
  for p in range(n):
    #Matriz U:
    for j in range(p,n):
      soma=0
      if p!=0:
        for k in range(p):
          soma = soma + L[p][k]*U[k][j]
      U[p][j] = A[p][j] - soma

    #Matriz L:
    for i in range(p+1,n):
      soma=0
      if p!=0:
        for k in range(p):
          soma = soma + L[i][k]*U[k][p]
      L[i][p] = (A[i][p] - soma)/U[p][p]

  return L,U

#Calculo do Determinante da Matriz
def DetA(U):
  n=len(U)
  detA=1
  for i in range(n):
    detA = detA*U[i][i];
  return detA

# A = np.array([[3,3,1],[2,2,-1],[1,-1,5]], dtype=float)
# b=np.array([7,3,5],dtype=float)
# x = EliminacaoGauss(A,b)
#L,U=DecomposicaoLU(A)
#detA = DetA(U)
#y = SistemaTriangularInferior(L,b)
#x = SistemaTriangularSuperior(U,y)
#print(L)
#print(U)
#print(y)
# print(x)


#Eliminação de Gauss
def EliminacaoGauss(A,b):
  n = len(b)
  for k in range(n-1):
    for i in range(k+1,n):
      aux = A[i,k]
      for j in range(k,n):
        A[i][j] = A[i][j] - A[k][j] * (aux/A[k][k])
      b[i] = b[i] - b[k]*(aux/A[k][k])
  x = SistemaTriangularSuperior(A,b)
  print(A)
  print(b)
  return x

A = np.array([[3,3,1],[2,2,-1],[1,-1,5]], dtype=float)
b=np.array([7,3,5],dtype=float)
x = EliminacaoGauss(A,b)
print(x)