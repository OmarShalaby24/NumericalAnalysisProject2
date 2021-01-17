from GaussianJordan import *
from GaussElimination import *
from GaussSeidel import *
from LU import *
from plot import *


def methods_win(iter=50, errors=0.00001, initPoint=[0, 0, 0]):
    def solve_all():
        output_win = Tk()
        output_win.title("NUMERICAL METHODS")
        output_win.configure(bg="#B7C3D0")
        output_win.geometry("1000x700")

        results = Label(output_win, text="RESULTS\n*output windows are scrollable*", bg="#B7C3D0", fg="black")
        results.place(x=400, y=15)

        output = Text(output_win, width=80, height=8.5, wrap=WORD, background="white")
        output.place(x=160, y=50)
        output2 = Text(output_win, width=80, height=8.5, wrap=WORD, background="white")
        output2.place(x=160, y=205)
        output3 = Text(output_win, width=80, height=8.5, wrap=WORD, background="white")
        output3.place(x=160, y=360)
        output4 = Text(output_win, width=120, height=8.5, wrap=WORD, background="white")
        output4.place(x=15, y=515)

        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()
        output.delete(0.0, END)
        output.insert(END, '**Gauss Elimination**\n\n')
        output.insert(END, GaussianElimination(int(unknownsNoField), equationField))

        unknownsNoField = unknownsEntry2.get()
        equationField = equEntry2.get()
        output2.delete(0.0, END)
        output2.insert(END, '**Gauss Jordan**\n\n')
        output2.insert(END, gauss_jordan(int(unknownsNoField), equationField))

        unknownsNoField = unknownsEntry3.get()
        equationField = equEntry3.get()
        output3.delete(0.0, END)
        output3.insert(END, '**LU Without pivoting**\n\n')
        output3.insert(END, LU(inputToMatrix(int(unknownsNoField), equationField)))
        output3.insert(END, '\n\n**LU With pivoting**\n\n')

        unknownsNoField = unknownsEntry3.get()
        equationField = equEntry3.get()
        output3.insert(END, lu_pivoting(int(unknownsNoField), equationField))

        unknownsNoField = unknownsEntry4.get()
        equationField = equEntry4.get()
        iterationsField = iterationsEntry.get()
        epsilonField = epsilonEntry.get()
        initialValField = initialValEntry.get()
        initPoints = initialValField
        x = initPoints.split()
        initPoints = []
        for i in range(0, int(unknownsNoField)):
            initPoints.append(float(x[i]))
        output4.delete(0.0, END)
        output4.insert(END, '***Gauss Seidel**\n\n')
        y = function(equationField, int(unknownsNoField), int(iterationsField), float(epsilonField),
                     initPoints)
        for i in range(len(y)):
            output4.insert(END, y[i])

    window = Tk()
    window.title("NUMERICAL METHODS")
    window.configure(bg="#B7C3D0")
    window.geometry("1300x500")

    m_label = Label(window, text="Gauss Elimination Method", bg="#162252", fg="white", font=(15))
    m_label.place(x=203, y=20)

    uknowns_label = Label(window, text="1.Enter number of unknowns", bg="#B7C3D0", fg="black")
    uknowns_label.place(x=220, y=70)

    unknownsEntry = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry.place(x=205, y=95)

    equations_label = Label(window, text="2.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label.place(x=170, y=150)

    equEntry = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry.place(x=35, y=175)

    line = Label(window,
                 text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                 bg="#B7C3D0", fg="#162252")
    line.place(x=70, y=205)

    m_label2 = Label(window, text="Gauss Jordan Method", bg="#162252", fg="white", font=(15))
    m_label2.place(x=895, y=20)

    uknowns_label2 = Label(window, text="1.Enter number of unknowns", bg="#B7C3D0", fg="black")
    uknowns_label2.place(x=900, y=70)

    unknownsEntry2 = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry2.place(x=880, y=95)

    equations_label2 = Label(window, text="2.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label2.place(x=850, y=150)

    equEntry2 = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry2.place(x=710, y=175)

    m_label3 = Label(window, text="LU Decomposition Method", bg="#162252", fg="white", font=(15))
    m_label3.place(x=203, y=230)

    uknowns_label3 = Label(window, text="1.Enter number of unknowns", bg="#B7C3D0", fg="black")
    uknowns_label3.place(x=220, y=270)

    unknownsEntry3 = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry3.place(x=205, y=295)

    equations_label3 = Label(window, text="2.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label3.place(x=170, y=350)

    equEntry3 = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry3.place(x=35, y=375)

    m_label4 = Label(window, text="Gauss Seidel Method", bg="#162252", fg="white", font=(15))
    m_label4.place(x=897, y=230)

    uknowns_label4 = Label(window, text="1.Enter number of unknowns", bg="#B7C3D0", fg="black")
    uknowns_label4.place(x=900, y=270)

    unknownsEntry4 = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry4.place(x=880, y=295)
    # unknownsEntry4.insert(0, noOfV)

    equations_label4 = Label(window, text="2.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label4.place(x=850, y=350)

    equEntry4 = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry4.place(x=710, y=375)
    # equEntry4.insert(0, eqs)

    iterations_label = Label(window, text="3.Enter iteration no.", bg="#B7C3D0", fg="black")
    iterations_label.place(x=705, y=415)

    iterationsEntry = Entry(window, width=5, bg="white", borderwidth=3)
    iterationsEntry.place(x=820, y=415)
    iterationsEntry.insert(0, str(iter))

    epsilon_label = Label(window, text="4.Enter epsilon", bg="#B7C3D0", fg="black")
    epsilon_label.place(x=860, y=415)

    epsilonEntry = Entry(window, width=15, bg="white", borderwidth=3)
    epsilonEntry.place(x=945, y=415)
    epsilonEntry.insert(0, str(errors))

    initialVal_label = Label(window, text="5.Enter initial values", bg="#B7C3D0", fg="black")
    initialVal_label.place(x=1050, y=415)

    initialValEntry = Entry(window, width=15, bg="white", borderwidth=3)
    initialValEntry.place(x=1160, y=415)
    initialValEntry.insert(0, initPoint)

    solve_btn = Button(window, text="Solve", width=20, height=1, bg="#162252", fg="white", command=solve_all)
    solve_btn.place(x=570, y=455)
