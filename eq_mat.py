import re
import numpy


def equationToMatrix(numberOfVariables, eq):
    rows, cols = (numberOfVariables, numberOfVariables + 1)
    A = numpy.empty(shape=(numberOfVariables, numberOfVariables + 1))
    for i in range(0, numberOfVariables):
        coefs = re.findall(r'[0-9\-\+]+', eq[i])
        # print(coefs)
        for j in range(0, numberOfVariables + 1):
            if coefs[j] == "+" or coefs[j] == "-":
                coefs[j] = coefs[j] + "1"
            elif len(coefs) < numberOfVariables + 1:
                coefs.insert(0, "1")
            A[i][j] = int(coefs[j])
            # print(A[i][j])
    return A


def inputToMatrix(numberOfVariables, eqnuations):
    # n = int(input('Enter number of unknowns: '))
    matrix = numpy.zeros((numberOfVariables, numberOfVariables + 1))
    eqnNum = 0
    # out = numpy.zeros(n)
    # input = input('Enter your equations separated by "," ')
    equations = eqnuations.split(',')

    count = 0
    for _ in equations:
        equations[count] = '+' + equations[count]
        count += 1

    # print(equations)
    for i in equations:
        eqnCoef = re.findall(r'[0-9\-\+]+', i)
        # print(z)

        coef = 0
        for j in eqnCoef:
            if j == '-':
                eqnCoef[coef] = '-1'
            elif j == '+':
                eqnCoef[coef] = '1'
            elif j == '+-':
                eqnCoef[coef] = '-1'
            elif len(j) > 2 & j.find('+-'):
                eqnCoef[coef] = j[1:]
            matrix[eqnNum][coef] = int(eqnCoef[coef])
            coef += 1
        # print(token)
        eqnNum += 1
    return matrix
