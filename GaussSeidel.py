# as A matrix, Solution and B matrix
from eq_mat import inputToMatrix
import plot
import copy
from tkinter import *


# "4x+y+2z-4,3x+5y+z-7,x+y+3z-3"


def seidel(a, x):
    # n is the number of equations
    n = len(a)

    for j in range(0, n):
        temp = a[j][n]

        for i in range(0, n):
            if (j != i):
                temp -= a[j][i] * x[i]
            # updating the value of our solution
        x[j] = temp / a[j][j]
    # updated solution
    return x


def function(equations, numOfEq, numOfIterations, epsilon, initialValues):
    # n is the number of equations
    x = initialValues
    n = numOfEq
    output = list()
    output.append("i  ")
    for i in range(numOfEq):
        output.append("\troot%d" % (i+1))
    output.append("\trelative error:\t\t")
    for i in range(numOfEq):
        output.append("  root%d\t\t" % (i+1))
    output.append("\n")
    initialValues = []
    a = inputToMatrix(n, equations)
    listA = [None] * n
    listLength = listA.__len__()
    l = 0
    while l < n:
        listA[l] = []
        l += 1

    index2 = 0
    oldX = []
    flag = True

    # specify the number of iteration
    for i in range(0, numOfIterations):
        x = seidel(a, x)
        output.append("%d  " % i)
        for k in range(len(x)):
            output.append("%f \t" % x[k])
        k = 0
        relativeEr = []
        for j in x:
            if not flag:
                error = abs((x[k] - oldX[k]) / x[k])
                relativeEr.append(error)
            listA[k].append([i, j])
            k += 1
        index2 = index2 + 1

        # print each time the updated solution
        output.append("\t\t\t")
        if not flag:
            for k in range(len(x)):
                output.append("%f\t\t" % relativeEr[k])
        else:
            for k in range(len(x)):
                output.append("  --\t\t")
        oldX = copy.deepcopy(x)
        output.append("\n")

        relErFlag = True
        if not flag:
            for value in relativeEr:
                if value > epsilon:
                    relErFlag = False

        if relErFlag and not flag:
            break
        flag = False

    obj = plot.plot(listA)
    obj.draw()

    f = open("SeidelOutput.txt", "w")
    y = output
    for i in range(len(y)):
        f.write(str(y[i]))
    f.close()
    return output


############# GUI #############
def gauss_seidel_win(noOfV=0, eqs="", iter=50, errors=0.00001, initPoint=[0, 0, 0]):
    def clickGaussSeidel():
        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()
        iterationsField = iterationsEntry.get()
        epsilonField = epsilonEntry.get()
        initialValField = initialValEntry.get()
        initPoints = initialValField
        x = initPoints.split()
        initPoints = []
        for i in range(0, int(unknownsNoField)):
            initPoints.append(float(x[i]))
        output.delete(0.0, END)
        y = function(equationField, int(unknownsNoField), int(iterationsField), float(epsilonField), initPoints)
        for i in range(len(y)):
            output.insert(END, y[i])

    window = Tk()
    window.title("Gauss Seidel Method")
    window.configure(bg="#B7C3D0")
    window.geometry("800x750")

    m_label = Label(window, text="Gauss Seidel Method", bg="#162252", fg="white", font=(15))
    m_label.place(x=317, y=20)

    uknowns_label = Label(window, text="1.Enter number of equations", bg="#B7C3D0", fg="black")
    uknowns_label.place(x=313, y=70)

    unknownsEntry = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry.insert(0, noOfV)
    unknownsEntry.place(x=300, y=95)

    equations_label = Label(window, text="2.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label.place(x=290, y=150)

    equEntry = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry.insert(0, eqs)
    equEntry.place(x=125, y=175)

    iterations_label = Label(window, text="3.Enter number of iterations", bg="#B7C3D0", fg="black")
    iterations_label.place(x=320, y=230)

    iterationsEntry = Entry(window, width=15, bg="white", borderwidth=3)
    iterationsEntry.insert(0, str(iter))
    iterationsEntry.place(x=350, y=255)

    epsilon_label = Label(window, text="4.Enter epsilon", bg="#B7C3D0", fg="black")
    epsilon_label.place(x=355, y=310)

    epsilonEntry = Entry(window, width=15, bg="white", borderwidth=3)
    epsilonEntry.insert(0, str(errors))
    epsilonEntry.place(x=350, y=335)

    initialVal_label = Label(window, text="5.Enter initial values", bg="#B7C3D0", fg="black")
    initialVal_label.place(x=340, y=390)

    initialValEntry = Entry(window, width=15, bg="white", borderwidth=3)
    initialValEntry.insert(0, initPoint)
    initialValEntry.place(x=350, y=415)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#162252", fg="white",
                       command=clickGaussSeidel)
    solve_btn.place(x=320, y=470)

    output = Text(window, width=100, height=15, wrap=WORD, background="white")
    output.place(x=0, y=510)

    window.mainloop()
