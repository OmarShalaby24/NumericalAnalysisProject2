def readMatrixData(filename="Iterative.txt", isSeidle = False):
    f = open(filename)
    noOfEquations = int(f.readline())
    method = f.readline()
    method = method[:-1]

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
        error = f.readline()
        x = error.split()
        error = []
        for i in range(0, noOfEquations):
            error.append(float(x[i]))
        initPoints = f.readline()
        x = initPoints.split()
        initPoints = []
        for i in range(0, noOfEquations):
            initPoints.append(float(x[i]))

        f.close()
        return noOfEquations, string, method, error, initPoints

    f.close()
    return noOfEquations, string, method
    # exp = f.readline()
    # textEntry.delete(0, END)
    # textEntry.insert(0, exp)
    # exp = f.readline()
    # firstLimit.delete(0, END)
    # firstLimit.insert(0, exp)
    # exp = f.readline()
    # secondLimit.delete(0, END)
    # secondLimit.insert(0, exp)
    # exp = f.readline()
    # epsilon.delete(0, END)
    # epsilon.insert(0, exp)
    # exp = f.readline()
    # iterations.delete(0, END)
    # iterations.insert(0, exp)


file1 = "input.txt"
file2 = "Iterative.txt"

n, eq, method = readMatrixData(file1)
print(n)
print(method)
print(eq)

print("-----------------------------------")

n, eq, method, errors, init = readMatrixData(file2,True)
print(n)
print(method)
print(eq)
print(errors)
print(init)
# print(len(method))
