from numpy import matrix, linalg
import numpy as np

print("Solução pelo Método de Gauss-Jordan")
mA = np.array([[2.0, 1.0, 1.0], [0.3, 2.0, 0.25], [1.0, 1.0, 2.0]])
mB = np.array([[39.0], [13.0], [45.0]])

print(mA)
print(mB)

print("Matriz = A * X = B")
print("Gauss-Jordan => I*X = S")
print("I*X = (A-1 * A)*x")
print("S = A-1 * B")

inMA = np.linalg.inv(mA)
print("\nA-1:")
print(inMA)
mS = np.matmul(inMA, mB)
print("\nS:")
print(mS)