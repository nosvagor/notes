from fractions import Fraction

import linearFunctions as lf
import numpy as np
import sympy as sp

# --- Question 2.1.26 --- #
print("\n" + "-" * 19)
print("Question 2.1.26:\n")

A = sp.Matrix(
    [
        [1, 0, 0],
        [2, 4, 0],
        [3, 2, 1],
    ]
)

B = sp.Matrix(
    [
        [2, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
)
AB = A @ B

lf.dimCA(A)
lf.dimCA(B)
lf.dimNA(B)
lf.dimCA(AB)
print("-" * 19)

# --- Question 2.3.13 --- #
print("\n" + "-" * 19)
print("Question 2.3.13:\n")

A = sp.Matrix(
    [
        [1, 1, 0],
        [1, 3, 1],
        [3, 1, -1],
    ]
)

U = sp.Matrix(
    [
        [1, 1, 0],
        [0, 2, 1],
        [0, 0, 0],
    ]
)

lf.dimCA(A)
lf.dimCA(U)
lf.dimCAT(A)
lf.dimCAT(U)

print(np.array(U.rref()[0]), "\n")
print("-" * 19)

# --- Question 2.4.14 --- #
print("\n" + "-" * 19)
print("Question 2.4.14:\n")

A = np.array(
    [
        [1, 1, 0],
        [0, 1, 1],
    ]
)

M = np.array(
    [
        [1, 0],
        [1, 1],
        [0, 1],
    ]
)

a, b, c, d, e, x, y, z, t = sp.symbols("a b c d e x y z t")

T = sp.Matrix(
    [
        [a, b],
        [0, a],
    ]
)

with np.printoptions(
    formatter={"all": lambda x: str(Fraction(x).limit_denominator())}
):
    print(np.linalg.inv(A @ A.T), "\n")
    print(np.linalg.inv(M.T @ M), "\n")

print(np.array(T.inv()), "\n")
print("-" * 19)
