import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix, csc_matrix, csr_matrix
from scipy.sparse.linalg import splu, spsolve

# ┌┬┐┌─┐┌─┐┬┌─
#  │ ├─┤└─┐├┴┐
#  ┴ ┴ ┴└─┘┴ ┴
# Write an iterative algorithm for solving Ax=b for a given sparse s.p.d matrix
# A stored in sparse format.

# The function should take as input:
# - matrix
# - maximal number of iterations
# - and tolerance
# Returns:
# - number of iterations
# - residual norm
# - accuracy


def read_matrix(filepath, csr=False, csc=False):
    df = pd.read_csv(filepath, sep=" ", header=None)
    df.columns = ["col", "row", "data"]
    matrix = coo_matrix((df["data"], (df["row"], df["col"])))

    if csr:
        return matrix.tocsr()
    if csc:
        return matrix.tocsc()

    return matrix


# Dense implementation of Gauss - Seidel
def gauss_seidel(A, b, tolerance=1e-16, max_iterations=1000):

    # initial x vector
    x = np.zeros_like(b, dtype=np.double)  # zeros work fine
    # x = np.random.rand(A.shape[0], 1)    # can be random though

    # iteration count, not necessary but useful to see how many were needed
    iter_count = 0

    # iterate, solving for x_k
    for k in range(max_iterations):

        # initialize: x_{k-1} and x_k
        x_prev = x.copy()

        # loop over rows
        for i in range(A.shape[0]):
            # using wiki forward sub formula:
            # https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method#Description
            row_sum = A[i, :i] @ x[:i]
            row_sum_prev = A[i, (i + 1) :] @ x_prev[(i + 1) :]
            x[i] = (b[i] - row_sum - row_sum_prev) / A[i, i]

        iter_count += 1

        # relative residual between iterations
        residual = np.linalg.norm(x - x_prev)

        # overall residual (current accuracy)
        accuracy = residual / np.linalg.norm(x)

        # Stop condition
        if accuracy < tolerance:
            break

    return (
        x,
        iter_count,
        residual,
        accuracy,
    )


###############################################################################

# ┌┬┐┌─┐┌─┐┌┬┐┬┌┐┌┌─┐
#  │ ├┤ └─┐ │ │││││ ┬
#  ┴ └─┘└─┘ ┴ ┴┘└┘└─┘

np.random.seed(420)

A = read_matrix("data/25.txt", csc=True)  # splu().solve() wants csc
b = np.random.rand(A.shape[0])

x_c, iterations, residual, accuracy = gauss_seidel(A, b)

print(f"\niterations:\t {iterations}\nresidual:\t {residual}\naccuracy:\t {accuracy}")

# x_s = splu(A).solve(b)
x_s = spsolve(A, b)

print(f"\nDifference between scipy and custom: {np.linalg.norm(x_c - x_s)}")
