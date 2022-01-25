import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix, csc_matrix, csr_matrix
from scipy.sparse.linalg import splu


def read_matrix(filepath, csr=False, csc=False):
    df = pd.read_csv(filepath, sep=" ", header=None)
    df.columns = ["col", "row", "data"]
    matrix = coo_matrix((df["data"], (df["row"], df["col"])))

    if csr:
        return matrix.tocsr()
    if csc:
        return matrix.tocsc()

    return matrix


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
