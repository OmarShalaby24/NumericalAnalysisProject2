import pprint
import numpy as np
import scipy.linalg  # SciPy Linear Algebra Library

def lu_pivoting(A,B):

    A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
    B = np.array([25, -10, -4])

    P, L, U = scipy.linalg.lu(A)

    d = np.linalg.inv(L).dot(B)
    X = np.linalg.inv(U).dot(d)
    return X

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
