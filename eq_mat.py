import re
import numpy

def equationToMatrix(numberOfVariables,eq):
    rows,cols = (numberOfVariables,numberOfVariables+1)
    A = numpy.empty(shape=(numberOfVariables,numberOfVariables+1))
    for i in range(0,numberOfVariables):
        coefs =re.findall(r'[0-9\-\+]+', eq[i])
        #print(coefs)
        for j in range(0,numberOfVariables+1):
            if coefs[j] == "+" or coefs[j] == "-":
                coefs[j] = coefs[j]+"1"
            elif len(coefs)<numberOfVariables+1:
                coefs.insert(0,"1")
            A[i][j] = int(coefs[j])
            #print(A[i][j])
    return A