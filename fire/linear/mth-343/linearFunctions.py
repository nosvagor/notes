import numpy as np
import sympy as sp
from termcolor import colored


def linearDependence(a, b, c):
    print("-" * 30)
    a = np.array([a])
    b = np.array([b])
    c = np.array([c])

    u, v, w = sp.symbols("u,v,w")
    symbolic = np.array([u, v, w])

    A = np.concatenate((a, b, c))
    print(A)
    print("  rref 🠗")
    print(np.array(sp.Matrix(A).rref()[0]))
    # check leftnullspace for linear dependence
    # return vector required to reach zero vector if true
    ANul = np.array(sp.Matrix(A.T).nullspace())
    if len(ANul) >= 1:
        cokernel = ANul[0].T[0]
        print(f"\nleft nullspace = {cokernel}")
        print(f"\n{symbolic@cokernel} = 0")
        print("-" * 30)
    else:
        print("\nVectors are linearly independent")
        print("-" * 30)


def nodiag_view(a):
    m = a.shape[0]
    p, q = a.strides
    return np.lib.stride_tricks.as_strided(a[:, 1:], (m - 1, m), (p + q, q))


def isOrthogonal(A, normalized=False):
    Q, R = np.linalg.qr(A)
    R = np.array(R, dtype=int)
    print(f"R from QR decomp should be diagonal, i.e.,\n{R}")
    orthog_set = (nodiag_view(R) == 0).all()
    print(f"\nIs R diagonal (and full rank)? {orthog_set}\n")
    if orthog_set and np.linalg.matrix_rank(R) == np.shape(A[2]):
        print(colored("{u,v,w} is orthogonal\n", "green"))
        if normalized:
            print(colored(f"normalized  ↓ \n{np.array(Q)}", "green"))
        print("\n", "-" * 20, "\n")
    else:
        print(colored("{u,v,w} is not orthogonal\n", "red"))
        notOrthogonal(A)


def notOrthogonal(A):
    u, v, w = A[:, 0], A[:, 1], A[:, 2]
    if not u @ v == 0:
        print(colored(f"u@v = {u@v}", "red"))
    elif not u @ w == 0:
        print(colored(f"u@w = {u@w}", "red"))
    elif not v @ w == 0:
        print(colored(f"v@w = {v@w}", "red"))

    print("\n", "-" * 20, "\n")


def dimCA(A):
    CA = A.columnspace()
    print(f"Dimension of the columnspace = {len(CA)}\n")
    for i in range(len(CA)):
        print(np.array(CA)[i], "\n")


def dimCAT(A):
    CAT = A.rowspace()
    print(f"Dimension of the rowspace = {len(CAT)}\n")
    for i in range(len(CAT)):
        print(np.array(CAT)[i].T, "\n")


def dimNA(A):
    NA = A.nullspace()
    print(f"Dimension of the nullspace (kernel) = {len(NA)}\n")
    for i in range(len(NA)):
        print(np.array(NA)[i], "\n")
