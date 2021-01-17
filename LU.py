import pprint
import numpy as np
import scipy.linalg  # SciPy Linear Algebra Library
from eq_mat import *
from tkinter import *


# 3x+2y+2z+4,2x-5y+4z-6,6x-8y+7z-12

def lu_pivoting(n, equations):
    matrix = inputToMatrix(n, equations)
    A = np.zeros(shape=(len(matrix), len(matrix)))
    B = np.zeros(shape=(len(matrix), 1))
    for i in range(len(matrix)):
        for k in range(len(A)):
            A[i][k] = matrix[i][k]
        B[i][0] = matrix[i][k + 1]

    print(len(A))
    print(matrix)
    print(A)
    print(B)

    P, L, U = scipy.linalg.lu(A)

    d = np.linalg.inv(L).dot(B)
    X = np.linalg.inv(U).dot(d)
    return X


def LU(mat):
    output = list()
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
                output.append("ERROR! Dividing by zero")
                return output
            ratio = coefs[i][k] / coefs[k][k]
            L[i][col - 1] = ratio
            for j in range(len(coefs[i])):
                coefs[i][j] -= ratio * coefs[k][j]

    # print(coefs)
    # print(L)

    D = np.linalg.inv(L).dot(values)
    result = np.linalg.inv(coefs).dot(D)
    output.append("U:\n")
    output.append(coefs)
    output.append("\nL:\n")
    output.append(L);
    output.append("\nResults:\n")
    output.append(result)
    f = open("LUOutput.txt", "w")
    y = output
    for i in range(len(y)):
        f.write(str(y[i]))
    f.close()
    return output


def lu_decomposition_win(noOfV=0, equ=""):
    def clickLUDecomposition():
        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()  # this will get the text from the text entry box
        output.delete(0.0, END)
        y = LU(inputToMatrix(int(unknownsNoField), equationField))
        for i in range(len(y)):
            output.insert(END, y[i])

    def clickLU_pivot():
        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()  # this will get the text from the text entry box
        output.delete(0.0, END)
        output.insert(END, lu_pivoting(int(unknownsNoField), equationField))

    window = Tk()
    window.title("LU Decomposition Method")
    window.configure(bg="#B7C3D0")
    window.geometry("600x500")

    m_label = Label(window, text="LU Decomposition Method", bg="#162252", fg="white", font=(15))
    m_label.place(x=202, y=20)

    uknowns_label = Label(window, text="1.Enter number of unknowns", bg="#B7C3D0", fg="black")
    uknowns_label.place(x=220, y=70)

    unknownsEntry = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry.insert(0, noOfV)
    unknownsEntry.place(x=205, y=95)

    equations_label = Label(window, text="1.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label.place(x=170, y=150)

    equEntry = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry.insert(0, equ)
    equEntry.place(x=25, y=175)

    solve_btn = Button(window, text="Solve without pivot", width=20, height=1, bg="#162252", fg="white",
                       command=clickLUDecomposition)
    solve_btn.place(x=130, y=230)

    solve_btn = Button(window, text="Solve with pivot", width=20, height=1, bg="#162252", fg="white",
                       command=clickLU_pivot)
    solve_btn.place(x=310, y=230)

    output = Text(window, width=90, height=15, wrap=WORD, background="white")
    output.place(x=0, y=265)
