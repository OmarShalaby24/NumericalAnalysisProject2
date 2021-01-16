# import tkinter as tk
from tkinter import *
import tkinter.font as font
from GaussianJordan import *
from GaussElimination import *
from FullAppGUI import *

root = Tk()

# to enter function

root.configure(bg="#B7C3D0")
root.geometry("400x300")

root.title("Numerical Analysis Methods")

label = Label(text="Choose a method for solution", bg="#B7C3D0", fg="black")
label.place(x=110, y=20)

gauss_elimination = Button(root, text="Gauss Elimination", width=20, height=2, bg="#162252", fg="white",
                           command=gauss_elimination_win)
gauss_elimination.place(x=118, y=50)

gauss_jordan = Button(root, text="Gauss Jordan", width=20, height=2, bg="#162252", fg="white",
                      command=gauss_jordan_win)
gauss_jordan.place(x=118, y=100)

lu_decomposition = Button(root, text="LU Decomposition", width=20, height=2, bg="#162252", fg="white")
lu_decomposition.place(x=118, y=150)

gauss_seidel = Button(root, text="Gauss Seidel", width=20, height=2, bg="#162252", fg="white")
gauss_seidel.place(x=118, y=200)

all_methods = Button(root, text="Solve for all methods", width=25, height=1, bg="#162252", fg="white",
                     command=methods_win)
all_methods.place(x=100, y=250)

root.mainloop()
