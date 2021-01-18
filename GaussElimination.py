# Importing NumPy Library
import numpy as np
import sys
from eq_mat import inputToMatrix
from tkinter import *


# "2x+y+4z-1,x+2x+3z-1.5,4x-y+2z-2"

def GaussianElimination(numberOfMatrix, equations):
    output = list()

    n = numberOfMatrix

    a = np.zeros((n, n + 1))

    x = np.zeros(n)

    a = inputToMatrix(numberOfMatrix, equations)

    # Applying Gauss Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            output.append('ERROR! Dividing by zero')
            return output

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

    # solution
    for i in range(n):
        output.append('Root%d = %0.3f' % (i + 1, x[i]))
    f = open("EliminationOutput.txt", "w")
    f.write(str(output))
    f.close()
    return output


############# GUI #############
def gauss_elimination_win(noOfV=0, eqs=""):
    def clickGaussElimination():
        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()
        output.delete(0.0, END)
        output.insert(END, GaussianElimination(int(unknownsNoField), equationField))

    window = Tk()
    window.title("Gauss Elimination Method")
    window.configure(bg="#B7C3D0")
    window.geometry("600x400")

    m_label = Label(window, text="Gauss Elimination Method", bg="#162252", fg="white", font=(15))
    m_label.place(x=203, y=20)

    uknowns_label = Label(window, text="1.Enter number of equations", bg="#B7C3D0", fg="black")
    uknowns_label.place(x=220, y=70)

    unknownsEntry = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry.insert(0, str(noOfV))
    unknownsEntry.place(x=205, y=95)

    equations_label = Label(window, text="1.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label.place(x=170, y=150)

    equEntry = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry.insert(0, eqs)
    equEntry.place(x=25, y=175)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#162252", fg="white",
                       command=clickGaussElimination)
    solve_btn.place(x=225, y=230)

    output = Text(window, width=90, height=8.5, wrap=WORD, background="white")
    output.place(x=0, y=265)

    window.mainloop()
