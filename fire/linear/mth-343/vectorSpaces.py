import numpy as np
import sympy as sp
import linearFunctions as my

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

my.dimCA(A)
my.dimCA(B)
my.dimNA(B)
my.dimCA(AB)

print("-" * 19)
