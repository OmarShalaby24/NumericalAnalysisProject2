def readMatrixData(filename="input2.txt"):
    f = open(filename)
    noOfEquations = int(f.readline())
    method = f.readline()
    method = method[:-1]

    isSeidle = False
    if (method == "gauss-Seidel"):
        isSeidle = True

    arrayOfEquations = []

    for i in range(0, noOfEquations):
        arrayOfEquations.append(f.readline())
        if arrayOfEquations[i][len(arrayOfEquations[i]) - 1] == '\n':
            arrayOfEquations[i] = arrayOfEquations[i][:-1]
    string = ""
    for i in range(0, noOfEquations):
        string += arrayOfEquations[i]
        if i != noOfEquations - 1:
            string += ","

    if isSeidle == True:
        print("is seidle = ", isSeidle)
        x = f.readline()
        iterations = int(x)
        er = f.readline()
        error = float(er)
        initPoints = f.readline()
        x = initPoints.split()
        initPoints = []
        for i in range(0, noOfEquations):
            initPoints.append(float(x[i]))

        f.close()
        return noOfEquations, string, method, iterations, error, initPoints

    f.close()
    return noOfEquations, string, method, 0, 0, 0
