import pprint
import numpy as np
import scipy.linalg  # SciPy Linear Algebra Library


def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""

    # Converts N into a list of tuples of columns
    tuple_N = zip(*N)

    # Nested list comprehension to calculate matrix multiplication
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]


def pivot_matrix(M):
    """Returns the pivoting matrix for M, used in Doolittle's method."""
    m = len(M)

    # Create an identity matrix, with floating point values
    id_mat = [[float(i == j) for i in range(m)] for j in range(m)]

    # Rearrange the identity matrix such that the largest element of
    # each column of M is placed on the diagonal of of M
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            # Swap the rows
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat


A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
B = np.array([25, -10, -4])
X = np.linalg.inv(A).dot(B)

P, L, U = scipy.linalg.lu(A)

d = np.linalg.inv(L).dot(B)
# print(d)

x = np.linalg.inv(U).dot(d)
print(x)


# print("L:",L)
# print("U:",U)
# L_inv = np.linalg.inv(L)
# U_inv = np.linalg.inv(U)

# print("inverse L:",L_inv)
# print(B)
# print(np.linalg.inv(L).dot(B))

def LU(mat):
    coefs = np.zeros(shape=(len(mat), len(mat)))
    values = np.zeros(shape=(len(mat), 1))
    for i in range(len(mat)):
        for k in range(len(coefs)):
            coefs[i][k] = mat[i][k]
        values[i][0] = mat[i][k + 1]
    col = 0
    L = np.zeros(shape=(len(coefs), len(coefs)))
    for i in range(0, len(coefs)):
        L[i][i] = 1.0
    for k in range(len(coefs)):
        col += 1
        for i in range(col, len(coefs)):
            if coefs[k][k] == 0:
                return 1
            ratio = coefs[i][k] / coefs[k][k]
            L[i][col - 1] = ratio
            for j in range(len(coefs[i])):
                coefs[i][j] -= ratio * coefs[k][j]

    # print(coefs)
    # print(L)

    D = np.linalg.inv(L).dot(values)
    output = np.linalg.inv(coefs).dot(D)
    print(output)
