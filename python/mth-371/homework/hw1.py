import numpy as np
import pandas
from scipy.linalg import lu, lu_factor, lu_solve
from scipy.sparse import csc_matrix, random
from scipy.sparse.linalg import splu, spsolve, spsolve_triangular


def read_data(filepath):
    data = pandas.read_csv(filepath, sep=" ", header=None)
    data.columns = ["col", "row", "data"]
    matrix = csc_matrix((data["data"], (data["row"], data["col"])))

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
            sumj = 0
            for j in range(i):
                sumj += L[i, j] * y[j]
            y[i] = (b[i] - sumj) / L[i, i]

        # backward sub
        for i in range(n - 1, -1, -1):
            sumj = 0
            for j in range(i + 1, n):
                sumj += U[i, j] * x[j]
            x[i] = (y[i] - sumj) / U[i, i]

        return x

    # Haven't adjusted for sparse, kinda of works still?
    # Np.sum(slice * x[i+1:n]) is essentially second for loop
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
b = np.random.rand(1, n)[0]

print(f"Matrix:\n {A}\n")

p, L, U = lu(A)
print(f"permutation: \n{p}\n")
print(f"lower: \n{L}\n")

x1 = solveLU(L, U, b, dense=True)
x2 = np.linalg.solve(A, b)
x3 = lu_solve(lu_factor(A), b)  # should be same as np.linalg.solve

print(f"given b: \n{b}\n")
print(f"x(custom): \n{x1}\n")
print(f"x_(np): \n{x2}\n")
print(f"x_(scipy): \n{x3}\n")
print(f"b_(A@x_custom): \n{A@x1}\n")
print(f"b_(A@x_np): \n{A@x2}\n")
print(
    "difference between output and ground truth is :",
    np.linalg.norm(b - A @ x2),
)

print("\n---SPARSE---\n")

n = 25
A = random(n, n, density=0.25, format="csc")
# A = read_data("data/25.txt")
b = np.random.rand(n, 1)
B = splu(A)
x_c = solveLU(B.L, B.U, b, sparse=True)
x_s = B.solve(b)

print(f"given b: \n{b.T[0]}\n")
print(f"x_custom: \n{x_c}\n")
print(f"x_(scipy.splu): \n{x_s.T[0]}\n")
print(f"b(A@x_scipy): \n{(A @ x_s).T[0]}\n")
print(
    "difference between output and ground truth is :",
    np.linalg.norm(b - A @ x_s),
)
