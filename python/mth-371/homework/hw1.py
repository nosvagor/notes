import numpy as np
import pandas
from scipy import stats
from scipy.linalg import lu, lu_factor, lu_solve
from scipy.sparse import coo_matrix, csc_matrix, random
from scipy.sparse.linalg import splu


def read_data(filepath):
    data = read_csv(filepath, sep=" ", header=None)
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


# Works on dense and sparse? Is there a difference?
def solveLU(L, U, b):
    n, _ = np.shape(L)
    y = np.zeros(n)
    x = np.zeros(n)

    for i in range(n):
        y[i] = (b[i] - np.sum(L[i, :i] * y[:i])) / L[i, i]

    # backward sub
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.sum(U[i, i + 1 : n] * x[i + 1 : n])) / U[i, i]

    return np.array(x)


###############################################################################


print("\n---DENSE---\n")

np.random.seed(420)

# # Load external data
A = read_data("data/25.txt")
n = 25

b = np.random.rand(n, 1)

# Decomposition into L, U
L, U = LU_factor(A)

# Back to dense for comparison
A = A.todense()

x_custom = solveLU(L, U, b)
x_np = np.linalg.solve(A, b)
x_scipy = lu_solve(lu_factor(A), b)  # should be same as np.linalg.solve

print(f"given b: \n{b.T}\n")
print(f"x(custom): \n{x_custom}\n")
print(f"x_(np): \n{x_np.T}\n")
print(f"x_(scipy): \n{x_scipy.T}\n")
print(f"b_(A@x_custom): \n{A@x_custom}\n")  # should be same as b
print(f"b_(A@x_np): \n{(A@x_scipy).T}\n")  # should be same as b

print("=" * 79)

print("\n---SPARSE---\n")

# Random sparse matrix
# n = 5
# A = random(n, n, density=0.25, format="csc")
# D = np.random.rand(n, 1)
# for i in range(n):
#     A[i, i] = D[i]

# Random sparse matrix
# n = 5
# A = random(n, n, density=0.25, format="csc")
# D = np.random.rand(n, 1)
# for i in range(n):
#     A[i, i] = D[i]


# Load external matrix
A = read_data("data/25.txt")
n = 25
b = np.random.rand(n, 1)

# custom
L, U = LU_factor(A)
x_c = solveLU(L, U, b)

# scipy
B = splu(A)
x_s = B.solve(b)

print(f"given b: \n{b.T[0]}\n")
print(f"x_custom: \n{x_c}\n")
print(f"x_(scipy.splu): \n{x_s.T[0]}\n")
print(f"b(p@A@x_custom): \n{A @ x_c}\n")
print(f"b(A@x_scipy): \n{(A @ x_s).T[0]}\n")
