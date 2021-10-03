import numpy as np
from sympy import *
from fractions import Fraction

a,b,c = symbols('a,b,c')

A = Matrix([
    [1,1,1,7],
    [1,2,2,10],
    [2,3,-4,3],
])

# b = np.array([
#     [2,5,7]
# ])

# x = Ainv@b.T
# Ainv = np.linalg.inv(A)
# print("A^-1=\n",Ainv)
# print("x =\n",x)

rrefA = Matrix(A).rref()
print(rrefA)
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
