# Importing NumPy Library
import numpy as np
import sys
from eq_mat import  inputToMatrix ,equationToMatrix

all_equations =["1x+1y-1z+3","6x+2y+2z-2","-3x+4y+1z-1"]


################code sha8al le guassian elimination#############
def GaussianElimination (numberOfMatrix,equations):
    # Reading number of unknowns

    n=numberOfMatrix
    # Making numpy array of n x n+1 size and initializing
    # to zero for storing augmented matrix
    a = np.zeros((n, n + 1))

    # Making numpy array of n size and initializing
    # to zero for storing solution vector
    x = np.zeros(n)

    # Reading augmented matrix coefficients
    print('Enter Augmented Matrix Coefficients:')
    a=equationToMatrix(numberOfMatrix,equations)
    # Applying Gauss Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    # Displaying solution
    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' % (i, x[i]), end='\t')

GaussianElimination(3,all_equations)
