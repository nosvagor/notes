from mth_371 import *

# ┌┬┐┌─┐┌─┐┌┬┐┬┌┐┌┌─┐
#  │ ├┤ └─┐ │ │││││ ┬
#  ┴ └─┘└─┘ ┴ ┴┘└┘└─┘

np.random.seed(420)

A = read_matrix("data/25.txt")
b = np.random.rand(A.shape[0])

x_c, iterations, residual, accuracy = gauss_seidel(A, b)

print(f"\niterations:\t {iterations}\nresidual:\t {residual}\naccuracy:\t {accuracy}")

x_s = spsolve(A, b)

print(f"\nDifference between scipy and custom: {np.linalg.norm(x_c - x_s)}")
