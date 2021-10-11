import numpy as np
import sympy as sp

a, b, c, d, e, x, y, z, t = sp.symbols("a b c d e x y z t")
k, m, n = sp.symbols("k m n", integer=True)
f, g, h = sp.symbols("f g h", cls=sp.Function)


# --- Question 6 --- #
print("\n" + "-" * 19)
print("Question 6:\n")

E = np.array(
    [
        [1, 0],
        [6, 1],
    ]
)

print(E ** 2, "\n")
print(E ** 8, "\n")
print(np.linalg.inv(E), "\n")

print("\n" + "-" * 19)

# --- Question 7 --- #
print("\n" + "-" * 19)
print("Question 7:\n")

F = np.array(
    [
        [1, 0, 0, 0],
        [2, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
)

G = np.array(
    [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 2, 1, 0],
        [0, 0, 0, 1],
    ]
)

H = np.array(
    [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 2, 1],
    ]
)

print(F @ G @ H, "\n")
print(H @ G @ F, "\n")

print("-" * 19)

# --- Question 18 --- #
print("\n" + "-" * 19)
print("Question 18:\n")

A = sp.Matrix(
    [
        [0, 1, -1, 2],
        [1, -1, 0, 2],
        [1, 0, -1, 2],
    ]
)
print(np.array(A.rref()[0]), "\n")

A = sp.Matrix(
    [
        [0, 1, -1, 0],
        [1, -1, 0, 0],
        [1, 0, -1, 0],
    ]
)
print(np.array(A.rref()[0]), "\n")

A = sp.Matrix(
    [
        [0, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 0, 1, 1],
    ]
)

print(np.array(A.rref()[0]), "\n")
print("\n" + "-" * 19)

# --- Question 1.5.33 --- #
print("\n" + "-" * 19)
print("Question 1.5.33:\n")

L = np.array(
    [
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 1],
    ]
)
U = L.T
b = np.array([[4, 5, 6]]).T
c = np.linalg.inv(L) @ b

print("c = \n", c, "\n")

x = np.linalg.inv(U) @ c

print("x = \n", x, "\n")

A = L @ U

print(A, "\n")
print("-" * 19)
