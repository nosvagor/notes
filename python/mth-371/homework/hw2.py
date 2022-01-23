import numpy as np
from pandas import read_csv
from scipy.sparse import coo_matrix, csr_matrix, random
from scipy.sparse.linalg import splu

# ┌┬┐┌─┐┌─┐┬┌─
#  │ ├─┤└─┐├┴┐
#  ┴ ┴ ┴└─┘┴ ┴
# Write an iterative algorithm for solving Ax=b for a given sparse s.p.d matrix
# A stored in csr format.
# The function should take as input:
# - matrix A, b,
# - initial iterate (x_0),
# - maximal number of iterations (max_iter),
# - and tolerance (tol).
# Returns:
# - number of iterations (iter_count)
# - residual norm (d)
# - accuracy (a)


def read_matrix(filepath):
    df = read_csv(filepath, sep=" ", header=None)
    df.columns = ["col", "row", "data"]
    A = coo_matrix((df["data"], (df["row"], df["col"]))).tocsr()
    return A


def gauss_seidel(A, b, tolerance=1e-16, max_iterations=1000):

    x = np.zeros_like(b, dtype=np.double)
    iter_count = 0

    # Iterate
    for k in range(max_iterations):

        x_old = x.copy()

        # Loop over rows
        for i in range(A.shape[0]):
            x[i] = (
                b[i]
                - np.dot(A[i, :i], x[:i])
                - np.dot(A[i, (i + 1) :], x_old[(i + 1) :])
            ) / A[i, i]

        iter_count += 1
        δ = np.linalg.norm(x - x_old, ord=np.inf)
        a = δ / np.linalg.norm(x, ord=np.inf)

        # Stop condition
        if a < tolerance:
            break

    return (
        x,
        iter_count,
        δ,
        a,
    )


###############################################################################

np.random.seed(420)

A = read_matrix("data/50.txt").tocsc()
A_d = A.todense()
b = np.random.rand(A_d.shape[0], 1)

x_c, iterations, δ, accuracy = gauss_seidel(A_d, b, tolerance=1e-16)

print(f"\niterations:\t {iterations}\nresidual:\t {δ}\naccuracy:\t {accuracy}")

x_s = splu(A).solve(b)

print(f"\nDifference between scipy and custom: {np.linalg.norm(x_c - x_s)}")
