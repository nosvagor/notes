import numpy as np
from sympy import *
from fractions import Fraction

a,b,c = symbols('a,b,c')

E = Matrix([
    [1,0,0],
    [a,1,0],
    [b,0,1],
])


F = Matrix([
    [1,0,0],
    [0,1,0],
    [0,c,1],
])

print(np.array(E**2))
# b = np.array([ rr
#     [2,5,7]
# ])

# x = Ainv@b.T
# Ainv = np.linalg.inv(A)
# print("A^-1=\n",Ainv)
# print("x =\n",x)

# rrefA = Matrix(A).rref()
# print(rrefA)
# print(np.array(rrefA[0]))

# RA = A.rowspace()
# print(f'Dimeionsion of rowspace = {len(RA)}\n')
# for i in range(len(RA)):
#     print(np.array(RA)[i].T,'\n')
# print('-'*20)

# NA = A.nullspace()
# print(f'Dimeionsion of nullspace = {len(NA)}\n')
# for i in range(len(NA)):
#     print(np.array(NA)[i],'\n')
# print('-'*20)

# CA = A.columnspace()
# print(f'Dimeionsion of columnspace = {len(CA)}\n')
# for i in range(len(CA)):
#     print(np.array(CA)[i],'\n')
# print('-'*20)


A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
])

B = np.array([
    [1,1,1],
    [4,2,0],
    [1,1,1],
])

C = np.array([
    [0,0,1],
    [0,1,0],
    [1,0,0],
])

D = np.array([
    [1,0,0],
    [-1,1,0],
    [-1,0,1],
])


E = np.array([
    [1,2,3],
    [1,3,1],
    [1,4,0],
])

print(C@A)
print(D@E)

