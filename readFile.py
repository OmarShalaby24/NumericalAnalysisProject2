def readMatrixData():
    f = open("input.txt")
    noOfEquations = int(f.readline())
    method = f.readline()
    method = method[:-1]

    arrayOfEquations = []

    for i in range(0,noOfEquations):
        arrayOfEquations.append(f.readline())
        if arrayOfEquations[i][len(arrayOfEquations[i]) - 1] == '\n':
            arrayOfEquations[i] = arrayOfEquations[i][:-1]

    f.close()
    return noOfEquations,arrayOfEquations,method
    #exp = f.readline()
    #textEntry.delete(0, END)
    #textEntry.insert(0, exp)
    #exp = f.readline()
    #firstLimit.delete(0, END)
    #firstLimit.insert(0, exp)
    #exp = f.readline()
    #secondLimit.delete(0, END)
    #secondLimit.insert(0, exp)
    #exp = f.readline()
    #epsilon.delete(0, END)
    #epsilon.insert(0, exp)
    #exp = f.readline()
    #iterations.delete(0, END)
    #iterations.insert(0, exp)

def readMatrixDataIterative():
    f = open("Iterative.txt")
    noOfEquations = int(f.readline())
    method = f.readline()
    method = method[:-1]

    arrayOfEquations = []

    for i in range(0,noOfEquations):
        arrayOfEquations.append(f.readline())
        if arrayOfEquations[i][len(arrayOfEquations[i])-1] == '\n':
            arrayOfEquations[i] = arrayOfEquations[i][:-1]

    lastline = f.readline()
    x = lastline.split()
    arg = []
    for i in range(0,len(x)):
        arg.append(float(x[i]))
    f.close()
    return noOfEquations, arrayOfEquations, method, arg

#n, eq, method, arg = readMatrixDataIterative()
n, eq, method = readMatrixData()
print(n)
print(method)
print(eq)
#print(arg)
#print(len(method))