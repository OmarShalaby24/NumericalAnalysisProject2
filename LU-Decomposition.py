import pprint
import numpy as np
import scipy.linalg  # SciPy Linear Algebra Library
import eq_mat


def lu_pivoting(n,equations):
    matrix = eq_mat.inputToMatrix(n,equations)
    A = np.zeros(shape=(len(matrix)-1, len(matrix)-1))
    B = np.zeros(shape=(len(matrix)-1, 1))
    for i in range(len(matrix)-1):
        for k in range(len(A)):
            A[i][k] = matrix[i][k]
        B[i][0] = matrix[i][k + 1]

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


X = lu_pivoting(4,"2x+5y+6z=7,6x+2y+3z=2,x+y+z=1")
print(X)