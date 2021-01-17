import numpy as np
import sys
import eq_mat as matrix
from tkinter import *

equations = "2x+5y-7,1x+3y-4"


def gauss_jordan(n, equations):
    # n = int(input('Enter number of unknowns: '))
    # print('Enter equations separated by comma:')
    # equations = input()

    output = list()
    Matrix = matrix.inputToMatrix(n, equations)

    # print(Matrix)

    result = np.zeros(n)

    for i in range(n):
        if Matrix[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            output.append('Divide by zero detected!')

        for j in range(n):
            if i != j:
                ratio = Matrix[j][i] / Matrix[i][i]

                for k in range(n + 1):
                    Matrix[j][k] = Matrix[j][k] - ratio * Matrix[i][k]

    for i in range(n):
        result[i] = Matrix[i][n] / Matrix[i][i]

    for i in range(n):
        output.append('Root%d = %0.3f' % (i+1, result[i]))
    print(output)
    return output


gauss_jordan(2, equations)


def gauss_jordan_win(noOfV=0, eqs=""):
    def clickGaussJordan():
        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()  # this will get the text from the text entry box
        output.delete(0.0, END)
        output.insert(END, gauss_jordan(int(unknownsNoField), equationField))

    window = Tk()
    window.title("Gauss Jordan Method")
    window.configure(bg="#B7C3D0")
    window.geometry("600x400")

    m_label = Label(window, text="Gauss Jordan Method", bg="#162252", fg="white", font=(15))
    m_label.place(x=220, y=20)

    uknowns_label = Label(window, text="1.Enter number of unknowns", bg="#B7C3D0", fg="black")
    uknowns_label.place(x=220, y=70)

    unknownsEntry = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry.insert(0, noOfV)
    unknownsEntry.place(x=205, y=95)

    equations_label = Label(window, text="1.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label.place(x=170, y=150)

    equEntry = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry.insert(0, eqs)
    equEntry.place(x=25, y=175)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#162252", fg="white", command=clickGaussJordan)
    solve_btn.place(x=225, y=230)

    output = Text(window, width=90, height=8.5, wrap=WORD, background="white")
    output.place(x=0, y=265)
