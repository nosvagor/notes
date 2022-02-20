import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix, csc_matrix, csr_matrix
from scipy.sparse.linalg import eigs, splu, spsolve


def read_data(filepath):
    data = pd.read_csv(filepath, sep=" ", header=None)
    data.columns = ["col", "row", "data"]
    vals = data["data"]
    cols = data["col"]
    rows = data["row"]

    if min(cols) == 1 and min(rows) == 1:
        cols = [i - 1 for i in cols]
        rows = [i - 1 for i in rows]

    return coo_matrix((vals, (cols, rows))).tocsr()


# ┬ ┬┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─  ┌─┐┌┐┌┌─┐
# ├─┤│ ││││├┤ ││││ │├┬┘├┴┐  │ ││││├┤
# ┴ ┴└─┘┴ ┴└─┘└┴┘└─┘┴└─┴ ┴  └─┘┘└┘└─┘
###############################################################################
def LU_factor(sparse_matrix):

    lu = splu(
        sparse_matrix.tocsc(),
        permc_spec="NATURAL",
        diag_pivot_thresh=0,
        options={"SymmetricMode": True},
    )
    return lu.L, lu.U


def solveLU(L, U, b):
    n, _ = np.shape(L)
    y = np.zeros(n)
    x = np.zeros(n)

    # forward sub
    for i in range(n):
        y[i] = (b[i] - np.sum(L[i, :i] * y[:i])) / L[i, i]

    # backward sub
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.sum(U[i, i + 1 : n] * x[i + 1 : n])) / U[i, i]

    return np.array(x)


# ┬ ┬┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─  ┌┬┐┬ ┬┌─┐
# ├─┤│ ││││├┤ ││││ │├┬┘├┴┐   │ ││││ │
# ┴ ┴└─┘┴ ┴└─┘└┴┘└─┘┴└─┴ ┴   ┴ └┴┘└─┘
###############################################################################
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


# ┬ ┬┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─  ┌┬┐┬ ┬┬─┐┌─┐┌─┐
# ├─┤│ ││││├┤ ││││ │├┬┘├┴┐   │ ├─┤├┬┘├┤ ├┤
# ┴ ┴└─┘┴ ┴└─┘└┴┘└─┘┴└─┴ ┴   ┴ ┴ ┴┴└─└─┘└─┘
###############################################################################
