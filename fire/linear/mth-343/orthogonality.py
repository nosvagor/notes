import numpy as np
import sympy as sp
import linearFunctions as lf

# --- Question 3.1.6 --- #
print("\n" + "-" * 19)
print("Question 3.1.6:\n")

a = np.array([1, 1, 1])
b = np.array([1, -1, 0])

# Confirming orthogonality
print("confirming orthogonality of given vectors\n", a @ b)
lf.proj(a, b)

# taking the cross product yields a perpendicular vector in R^3
c = np.cross(a, b)
print("\nOrthogonal basis", c, "\n")

print("dot products should = 0, projections should be 0")
print(a @ c)
lf.proj(a, c)
print(b @ c)
lf.proj(b, c)

print("\nfinding unit lengths")
print(f"||a||^2 = √{a.T @ a}")
print(f"||b||^2 = √{b.T @ b}")
print(f"||c||^2 = √{c.T @ c}")

print("-" * 19)

# --- Question 3.1.47 --- #
print("\n" + "-" * 19)
print("Question 3.1.47:\n")

a = np.random.randint(1, 3, size=(3))
b = np.random.randint(1, 3, size=(3))

c = np.cross(a, b)
d = np.cross(c, b)
e = np.cross(d, c)

A = np.array([c, d, e])

print(A, "\n")

# mutually exclusive?
print(c @ d, "\n")
print(c @ e, "\n")
print(d @ e, "\n")
print(np.array(sp.Matrix(A).rref()[0]), "\n")

# why does AA.T yield a diagonal
print(A @ A.T, "\n")

# why does A.TA yield a symmetric matrix? It should yield diagonal still, no?
print(A.T @ A, "\n")

# book example
B = np.array(
    [
        [2, 2, -1],
        [-1, 2, 2],
        [2, -1, 2],
    ]
)
print(B.T @ B, "\n")
print(B @ B.T, "\n")
print("-" * 19)
