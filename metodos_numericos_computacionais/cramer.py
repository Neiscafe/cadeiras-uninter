from numpy import matrix, linalg
import numpy as np

print("Solução pelo Método de Cramer")
mA = np.array([[2.0, 1.0, 1.0], [0.3, 2.0, 0.25], [1.0, 1.0, 2.0]])
mB = np.array([[39.0], [13.0], [45.0]])

print(mA)
print(mB)

mT = np.copy(mA);
mT[0][0] = mB[0][0]
mT[1][0] = mB[1][0]
mT[2][0] = mB[2][0]

print(mT)

mX = np.copy(mA);
mX[0][1] = mB[0][0]
mX[1][1] = mB[1][0]
mX[2][1] = mB[2][0]
print(mX)
mZ = np.copy(mA);
mZ[0][2] = mB[0][0]
mZ[1][2] = mB[1][0]
mZ[2][2] = mB[2][0]
print(mZ)
detA = np.linalg.det(mA)
detT = np.linalg.det(mT)
detX = np.linalg.det(mX)
detZ = np.linalg.det(mZ)

s1 = detT/detA
s2 = detX/detA
s3 = detZ/detA
print(fr"{s1} | {s2} | {s3}")