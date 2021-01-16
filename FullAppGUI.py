from GaussianJordan import *
from GaussElimination import *
from plot import *


def methods_win():
    def solve_all():
        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()  # this will get the text from the text entry box
        output.delete(0.0, END)
        output.insert(END, gauss_jordan(int(unknownsNoField), str(equationField)))

        unknownsNoField = unknownsEntry2.get()
        equationField = equEntry2.get()  # this will get the text from the text entry box
        output2.delete(0.0, END)
        output2.insert(END, GaussianElimination(int(unknownsNoField), str(equationField)))

    window = Tk()
    window.title("NUMERICAL METHODS")
    window.configure(bg="#B7C3D0")
    window.geometry("1300x800")

    m_label = Label(window, text="Gauss Jordan Method", bg="#162252", fg="white", font=(15))
    m_label.place(x=220, y=20)

    uknowns_label = Label(window, text="1.Enter number of unknowns", bg="#B7C3D0", fg="black")
    uknowns_label.place(x=220, y=70)

    unknownsEntry = Entry(window, width=30, bg="white", borderwidth=3)
    unknownsEntry.place(x=205, y=95)

    equations_label = Label(window, text="2.Enter your equations separated by a comma", bg="#B7C3D0", fg="black")
    equations_label.place(x=170, y=150)

    equEntry = Entry(window, width=90, bg="white", borderwidth=3)
    equEntry.place(x=35, y=175)

    # file_btn = Button(window, text="Load equation from file", width=20, height=1, bg="#53868B", fg="white",
    #                   command=readData)
    # file_btn.place(x=285, y=515)
    line = Label(window,
                 text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                 bg="#B7C3D0", fg="#162252")
    line.place(x=70, y=205)

    m_label2 = Label(window, text="Gauss Elimination Method", bg="#162252", fg="white", font=(15))
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
    iterations_label.place(x=750, y=415)

    iterationsEntry = Entry(window, width=15, bg="white", borderwidth=3)
    iterationsEntry.place(x=910, y=415)

    show_graph = Button(window, text="Show Graphs of iteration", width=20, height=1, bg="#162252", fg="white")
    show_graph.place(x=1050, y=413)

    solve_btn = Button(window, text="Solve", width=10, height=3, bg="#162252", fg="white", command=solve_all)
    solve_btn.place(x=605, y=575)

    # file_btn = Button(window, text="Load equation from file", width=20, height=1, bg="#53868B", fg="white",
    #                   command=hanging_line)
    # file_btn.place(x=605, y=625)

    output = Text(window, width=70, height=8.5, wrap=WORD, background="white")
    output.place(x=25, y=445)
    output2 = Text(window, width=70, height=8.5, wrap=WORD, background="white")
    output2.place(x=700, y=445)
    output3 = Text(window, width=70, height=8.5, wrap=WORD, background="white")
    output3.place(x=25, y=615)
    output4 = Text(window, width=70, height=8.5, wrap=WORD, background="white")
    output4.place(x=700, y=615)
