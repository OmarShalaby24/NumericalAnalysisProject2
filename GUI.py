from tkinter import *
import tkinter.font as font
from GaussianJordan import *
from GaussElimination import *
from LU import *
from GaussSeidel import *
import readFile
from FullAppGUI import *


def loadFile():
    scanFileEntry = fileEntry.get()
    noOfEquations, string, method, iterations, error, initPoints = readFile.readMatrixData(scanFileEntry)

    if method == "gauss-jordon":
        gauss_jordan_win(noOfEquations, string)
    elif method == "gauss-elimination":
        gauss_elimination_win(noOfEquations, string)
    elif method == "gauss-Seidel":
        gauss_seidel_win(noOfEquations, string, iterations, error, initPoints)
    elif method == "LU":
        lu_decomposition_win(noOfEquations, string)


root = Tk()
root.configure(bg="#B7C3D0")
root.geometry("400x400")
root.title("Numerical Analysis Methods")

label = Label(text="Choose a method for solution", bg="#B7C3D0", fg="black")
label.place(x=110, y=20)

gauss_elimination = Button(root, text="Gauss Elimination", width=20, height=2, bg="#162252", fg="white",
                           command=gauss_elimination_win)
gauss_elimination.place(x=118, y=50)

gauss_jordan = Button(root, text="Gauss Jordan", width=20, height=2, bg="#162252", fg="white",
                      command=gauss_jordan_win)
gauss_jordan.place(x=118, y=100)

lu_decomposition = Button(root, text="LU Decomposition", width=20, height=2, bg="#162252", fg="white",
                          command=lu_decomposition_win)
lu_decomposition.place(x=118, y=150)

gauss_seidel = Button(root, text="Gauss Seidel", width=20, height=2, bg="#162252", fg="white", command=gauss_seidel_win)
gauss_seidel.place(x=118, y=200)

all_methods = Button(root, text="Solve for all methods", width=25, height=1, bg="#162252", fg="white",
                     command=methods_win)
all_methods.place(x=100, y=260)

filelabel = Label(root, text="Enter file name", bg="#B7C3D0", fg="black")
filelabel.place(x=150, y=300)

fileEntry = Entry(root, width=30, bg="white", borderwidth=3)
fileEntry.insert(0, "input.txt")
fileEntry.place(x=100, y=320)

file_btn = Button(root, text="Load from file", width=25, height=1, bg="#162252", fg="white", command=loadFile)
file_btn.place(x=100, y=350)

root.mainloop()
