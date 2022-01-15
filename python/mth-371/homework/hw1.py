import numpy as np
import pandas
from scipy import stats
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

    # Haven't adjusted for sparse, but below is same as dense using slices.
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

np.random.seed(1123423)
n = 4
A = np.random.rand(n, n)
b = np.random.rand(1, n)[0]


print(f"Matrix:\n {A}\n")

p, L, U = lu(A)
print(f"permutation: \n{p}\n")
print(f"Lower matrix:\n {L}\n")

x1 = solveLU(L, U, b, dense=True)
x2 = np.linalg.solve(A, b)
x3 = lu_solve(lu_factor(A), b)  # should be same as np.linalg.solve

print(f"given b: \n{b}\n")
print(f"x(custom): \n{x1}\n")
print(f"x_(np): \n{x2}\n")
print(f"x_(scipy): \n{x3}\n")
print(f"b_(A@x_custom): \n{A@x1}\n")
print(f"b_(A@x_np): \n{A@x2}\n")

print("\n---SPARSE---\n")

n = 5
rvs = stats.poisson(4, loc=3).rvs
A = random(n, n, density=0.25, format="csc", data_rvs=rvs, dtype="int")

# make sure it's nonsingular by creating diagonal data entries
D = np.random.randint(1, 10, (1, n))[0]
for i in range(n):
    A[i, i] = D[i]

print("-" * 79)
print(f"Matrix(dense):\n{A.todense()}\n")
print(f"Matrix(csc):\n  (row, col)\t(data)\n\t\n{A}")
print("-" * 79, "\n")

# A = read_data("data/25.txt")
b = np.random.randint(1, 10, (n, 1))
B = splu(A)

print(f"L(dense):\n{B.L.todense()}\n")
print(f"U(dense):\n{B.U.todense()}\n")

x_c = solveLU(B.L, B.U, b, sparse=True)
x_s = B.solve(b)

print(f"given b: \n{b.T[0]}\n")
print(f"x_custom: \n{x_c}\n")
print(f"x_(scipy.splu): \n{x_s.T[0]}\n")
print(f"b(A@x_custom): \n{(A @ x_c).T}\n")
print(f"b(A@x_scipy): \n{(A @ x_s).T[0]}\n")
