import numpy as np
import sympy as sp

a, b, c, d, e, x, y, z, t = sp.symbols("a b c d e x y z t")
k, m, n = sp.symbols("k m n", integer=True)
f, g, h = sp.symbols("f g h", cls=sp.Function)


A = sp.Matrix(
    [
        [1, 0, 0],
        [a, 1, 0],
        [b, 0, 1],
    ]
)


B = sp.Matrix(
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, c, 1],
    ]
)

C = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 7, 9],
    ]
)

# --- Question 6 --- #
print("\n" + "-" * 19)
print("Question 6:\n")

E = np.array(
    [
        [1, 0],
        [6, 1],
    ]
)

print(E ** 2)

print("\n" + "-" * 19)
