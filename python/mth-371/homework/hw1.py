import numpy as np
import pandas
from scipy.linalg import lu
from scipy.sparse import coo_matrix, csc_matrix, random
from scipy.sparse.linalg import splu, spsolve, spsolve_triangular


def read_data(filepath):
    data = pandas.read_csv(filepath, sep=" ", header=None)
    data.columns = ["col", "row", "data"]
    matrix = csc_matrix((data["data"], (data["col"], data["row"])))

    return matrix


def LU_factor(sparse_matrix):

    lu = splu(
        sparse_matrix.tocsc(),
        permc_spec="NATURAL",
        diag_pivot_thresh=0,
        options={"SymmetricMode": True},
    )
    return lu.L, lu.U


def solveLU(L, U, b, dense=False, sparse=False):
    n, _ = np.shape(L)
    y = np.zeros(n)
    x = np.zeros(n)

    if dense:
        # forward sub
        for i in range(n):
            y[i] = (b[i] - np.sum(L[i, :i] * y[:i])) / L[i, i]

        # backward sub
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - np.sum(U[i, i + 1 : n] * x[i + 1 : n])) / U[i, i]

        return x

    # Haven't adjusted, copy of dense for now, almost works?
    if sparse:
        # forward sub
        for i in range(n):
            y[i] = (b[i] - np.sum(L[i, :i] * y[:i])) / L[i, i]

        # backward sub
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - np.sum(U[i, i + 1 : n] * x[i + 1 : n])) / U[i, i]

        return x

    else:
        print("Please select sparse or dense matrix")
        return b


###############################################################################


print("\n---DENSE---\n")

np.random.seed(1)
n = 4
A = np.random.rand(n, n)
b = np.ones(n)

print(f"Matrix:\n {A}\n")

_, L, U = lu(A)
x = solveLU(L, U, b, dense=True)

print(f"Lower matrix: \n{L} \n\nSolved: \n{x}")
print(f"Solved(np): \n{np.linalg.solve(A,b)}")
print(f"Ax = b: {A@x}\n")
print(
    "difference between output and ground truth is :",
    np.linalg.norm(b - A @ x),
)

print("\n---SPARSE---\n")

n = 20
A = random(n, n, density=0.25, format="csc")
A = read_data("data/25.txt")
b = np.ones((A.shape[0], 1))
B = splu(A)
x_s = B.solve(b)
x_c = solveLU(B.L, B.U, b, sparse=True)

print(f"Solved(custom): \n{x_c}\n")
print(f"Solved(scipy.splu): \n{x_s.T[0]}\n")
print(f"Ax=b: \n{(A @ x_s).T[0]}\n")
print(
    "difference between output and ground truth is :",
    np.linalg.norm(b - A @ x_s),
)
