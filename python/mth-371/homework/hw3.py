from mth_371 import *

# ┬ ┬┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─  ┌┬┐┬ ┬┬─┐┌─┐┌─┐
# ├─┤│ ││││├┤ ││││ │├┬┘├┴┐   │ ├─┤├┬┘├┤ ├┤
# ┴ ┴└─┘┴ ┴└─┘└┴┘└─┘┴└─┴ ┴   ┴ ┴ ┴┴└─└─┘└─┘
# Given a n×n symmetric sparse matrix A (one from the test matrices provided)

"""
1.  Form the following graph matrices associated with the sparsity pattern of
    A and store them in CSR format:
        - Adjacency matrix, A = (α_ij)
        - Edge-Vertex Connectivity matrix, E
        - Vertex-Edge Relation matrix, E^T
        - Diagonal matrix, D
        - Edge-Edge Adjacency matrix, A_E = EE^T
        - Finally, the Laplacian matrix, L = D − A.
"""


def adjacency(A_csr):
    return A


def edgeVertex(A):
    return EV


def edgeEdge(EV):
    A_E = EV.multiply(EV.T)
    return A_E


def diagonal(A):
    return D


def laplacian(D, A):
    L = D - A
    return L


# testing #####################################################################

from scipy.sparse.csgraph import laplacian

A = read_data("data/16x16.coo.txt")
L, D = laplacian(A, return_diag=True)

print(
    f"""
Lapacian (Head):

{L.tocsr()[1:5]}

Diagonal:

{D}
"""
)

##################################################################### testing #

"""
2.  Spectral clustering: compute d eigenvectors q1,q2...qd, corresponding to
    the first d minimal eigenvalues of the graph Laplacian L.
"""


def eigenvecs(L, k):
    return Q


# testing #####################################################################

eigenvectors = eigs(L, k=3, which="LM")[1]

print(
    f"""
Eigenvectors:

{eigenvectors}
    -> total eigenvectors: {len(eigenvectors)}
"""
)


##################################################################### testing #

"""
3.  K-means: The K-means algorithm generate n_c = K aggregates(groups of
    vertices). A1,A2...An. Create the following:
        - Relation matrix, P = vertex_aggregate
        - Coarse matrix Ac = P^TAP
"""


def aggregates(A_csr):
    return K


def relation(K):
    return P


def coarse(P, A):
    return A_c


# testing #####################################################################


##################################################################### testing #

"""
4. Visualize the graph.
"""

G = nx.from_scipy_sparse_matrix(L)
nx.draw(G)
plt.show()
