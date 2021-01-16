# Importing NumPy Library
import numpy as np
import sys
from eq_mat import inputToMatrix
from tkinter import *

all_equations = "2x+1y+4z-1,1x+2x+3z-1.5,4x-1y+2z-2"


################code sha8al le guassian elimination#############
def GaussianElimination(numberOfMatrix, equations):
    # Reading number of unknowns
    output = list()

    n = numberOfMatrix
    # Making numpy array of n x n+1 size and initializing
    # to zero for storing augmented matrix
    a = np.zeros((n, n + 1))

    # Making numpy array of n size and initializing
    # to zero for storing solution vector
    x = np.zeros(n)

    # Reading augmented matrix coefficients
    print('Enter Augmented Matrix Coefficients:')
    a = inputToMatrix(numberOfMatrix, equations)
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
        # print('X%d = %0.2f' % (i, x[i]), end='\t')
        output.append('Root%d = %0.3f' % (i, x[i]))
    print(output)
    return output


GaussianElimination(3,all_equations)


def gauss_elimination_win():
    def clickGaussElimination():
        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()  # this will get the text from the text entry box
        output.delete(0.0, END)
        output.insert(END, GaussianElimination(int(unknownsNoField), str(equationField)))

    window = Tk()
    window.title("Bisection Method")
    window.configure(bg="#B7C3D0")
    window.geometry("600x400")

    m_label = Label(window, text="Gauss Elimination Method", bg="#162252", fg="white", font=(15))
    m_label.place(x=200, y=20)

    uknowns_label = Label(window, text="1.Enter number of unknowns", bg="#B7C3D0", fg="black")
    uknowns_label.place(x=220, y=70)

    unknownsEntry = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry.place(x=205, y=95)

    equations_label = Label(window, text="1.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label.place(x=170, y=150)

    equEntry = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry.place(x=25, y=175)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#162252", fg="white",
                       command=clickGaussElimination)
    solve_btn.place(x=225, y=230)

    # file_btn = Button(window, text="Load equation from file", width=20, height=1, bg="#53868B", fg="white",
    #                   command=hanging_line)
    # file_btn.place(x=285, y=255)

    output = Text(window, width=90, height=8.5, wrap=WORD, background="white")
    output.place(x=0, y=265)

    window.mainloop()
