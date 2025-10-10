from numpy import matrix, linalg
import numpy as np
from numpy._core.defchararray import mod

print("Solução pelo Método de Gauss-Seidel")
mA = np.array([[2.0, 1.0, 1.0], [0.3, 2.0, 0.25], [1.0, 1.0, 2.0]])
mB = np.array([[39.0], [13.0], [45.0]])
t = 0.0
x = 0.0
n = 0.0
k = 0
mX0 = np.array([[t], [x], [n]])
erroT = 1
erroX = 1
erroN = 1
parada = False
print("Para conseguir as fórmulas, é necessário isolar uma de cada incógnita")
print("O módulo da incógnita selecionada deve ser maior ou igual à soma dos módulos das outras duas")

while parada==False:
  parada = erroT<0.0000000001 or erroX<0.0000000001or erroN<0.0000000001
  k1 = k+1
  t1 = (39-x-n)/2
  x1 = (13-(0.3*t1)-(0.25*n))/2
  n1 = (45-t1-x1)/2
