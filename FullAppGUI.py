from GaussianJordan import *
from GaussElimination import *
from GaussSiedal import *
from LU import *
from plot import *


def methods_win():
    def solve_all():
        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()  # this will get the text from the text entry box
        output.delete(0.0, END)
        output.insert(END, GaussianElimination(int(unknownsNoField), equationField))

        unknownsNoField = unknownsEntry2.get()
        equationField = equEntry2.get()  # this will get the text from the text entry box
        output2.delete(0.0, END)
        output2.insert(END, gauss_jordan(int(unknownsNoField), equationField))

        unknownsNoField = unknownsEntry3.get()
        equationField = equEntry3.get()  # this will get the text from the text entry box
        output3.delete(0.0, END)
        output3.insert(END, LU(inputToMatrix(int(unknownsNoField), equationField)))

        unknownsNoField = unknownsEntry4.get()
        equationField = equEntry4.get()  # this will get the text from the text entry box
        iterationsField = iterationsEntry.get()
        epsilonField = epsilonEntry.get()
        initialValField = initalValEntry.get()
        initPoints = initialValField
        x = initPoints.split()
        initPoints = []
        for i in range(0, int(unknownsNoField)):
            initPoints.append(float(x[i]))
        output.delete(0.0, END)
        output.insert(END, function(equationField, int(unknownsNoField), int(iterationsField), float(epsilonField),
                                    initPoints))

    window = Tk()
    window.title("NUMERICAL METHODS")
    window.configure(bg="#B7C3D0")
    window.geometry("1300x800")

    m_label = Label(window, text="Gauss Elimination Method", bg="#162252", fg="white", font=(15))
    m_label.place(x=220, y=20)

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
    m_label2.place(x=882, y=20)

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
    m_label4.place(x=890, y=230)

    uknowns_label4 = Label(window, text="1.Enter number of unknowns", bg="#B7C3D0", fg="black")
    uknowns_label4.place(x=900, y=270)

    unknownsEntry4 = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry4.place(x=880, y=295)

    equations_label4 = Label(window, text="2.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label4.place(x=850, y=350)

    equEntry4 = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry4.place(x=710, y=375)

    iterations_label = Label(window, text="3.Enter number of iterations", bg="#B7C3D0", fg="black")
    iterations_label.place(x=695, y=415)

    iterationsEntry = Entry(window, width=5, bg="white", borderwidth=3)
    iterationsEntry.place(x=850, y=415)

    epsilon_label = Label(window, text="4.Enter epsilon", bg="#B7C3D0", fg="black")
    epsilon_label.place(x=895, y=415)

    epsilonEntry = Entry(window, width=15, bg="white", borderwidth=3)
    epsilonEntry.place(x=990, y=415)

    initalVal_label = Label(window, text="5.Enter initial values", bg="#B7C3D0", fg="black")
    initalVal_label.place(x=1090, y=415)

    initalValEntry = Entry(window, width=15, bg="white", borderwidth=3)
    initalValEntry.place(x=1190, y=415)

    solve_btn = Button(window, text="Solve", width=10, height=3, bg="#162252", fg="white", command=solve_all)
    solve_btn.place(x=605, y=575)

    output = Text(window, width=70, height=8.5, wrap=WORD, background="white")
    output.place(x=25, y=445)
    output2 = Text(window, width=70, height=8.5, wrap=WORD, background="white")
    output2.place(x=700, y=445)
    output3 = Text(window, width=70, height=8.5, wrap=WORD, background="white")
    output3.place(x=25, y=615)
    output4 = Text(window, width=70, height=8.5, wrap=WORD, background="white")
    output4.place(x=700, y=615)
