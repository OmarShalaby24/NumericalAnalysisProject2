# as A matrix, Solution and B matrix
from eq_mat import inputToMatrix
import plot
import copy
from tkinter import *

equations = "4x+1y+2z-4,3x+5y+1z-7,1x+1y+3z-3"
x = [0, 0, 0]


def seidel(a, x):
    # Finding length of a(3)
    # n is the number of equations
    n = len(a)

    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable to store b[j]
        temp = a[j][n]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if (j != i):
                temp -= a[j][i] * x[i]
            # updating the value of our solution
        x[j] = temp / a[j][j]
    # returning our updated solution
    return x


def function(equations, numOfEq, numOfIterations, epsilon, initialValues):
    # n is the number of equations
    x = initialValues
    n = numOfEq
    output = list()
    output.append("i  ")
    for i in range(numOfEq):
        output.append("\tx%d" % i)
    output.append("\trelative error:\t\t")
    for i in range(numOfEq):
        output.append("  x%d\t\t" % i)
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
        print(x)
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
            print(relativeEr)
            for k in range(len(x)):
                output.append("%f\t\t" % relativeEr[k])
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

    print(output)
    obj = plot.plot(listA)
    obj.draw2()

    return output


def gauss_seidel_win(noOfV=0, eqs="", iter=50, errors=0.00001, initPoint=[0, 0, 0]):
    def clickGaussSeidel():
        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()  # this will get the text from the text entry box
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
    m_label.place(x=200, y=20)

    uknowns_label = Label(window, text="1.Enter number of unknowns", bg="#B7C3D0", fg="black")
    uknowns_label.place(x=220, y=70)

    unknownsEntry = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry.insert(0, noOfV)
    unknownsEntry.place(x=205, y=95)

    equations_label = Label(window, text="2.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label.place(x=170, y=150)

    equEntry = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry.insert(0, eqs)
    equEntry.place(x=25, y=175)

    iterations_label = Label(window, text="3.Enter number of iterations", bg="#B7C3D0", fg="black")
    iterations_label.place(x=175, y=230)

    iterationsEntry = Entry(window, width=15, bg="white", borderwidth=3)
    iterationsEntry.insert(0, str(iter))
    iterationsEntry.place(x=200, y=255)

    epsilon_label = Label(window, text="4.Enter epsilon", bg="#B7C3D0", fg="black")
    epsilon_label.place(x=200, y=310)

    epsilonEntry = Entry(window, width=15, bg="white", borderwidth=3)
    epsilonEntry.insert(0, str(errors))
    epsilonEntry.place(x=200, y=335)

    initialVal_label = Label(window, text="5.Enter initial values", bg="#B7C3D0", fg="black")
    initialVal_label.place(x=200, y=390)

    initialValEntry = Entry(window, width=15, bg="white", borderwidth=3)
    initialValEntry.insert(0, initPoint)
    initialValEntry.place(x=200, y=415)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#162252", fg="white",
                       command=clickGaussSeidel)
    solve_btn.place(x=225, y=470)

    output = Text(window, width=100, height=15, wrap=WORD, background="white")
    output.place(x=0, y=510)

    window.mainloop()
