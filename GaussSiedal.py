# as A matrix, Solution and B matrix
from eq_mat import inputToMatrix
import plot
import copy

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


def function(equations, numOfEq, numOfIterations, epsilon,initialValues):
    # int(input())input as number of variable to be solved
    # n is the number of equations
    x=initialValues
    n = numOfEq
    output = list()
    # a = []
    # b = []
    # initial solution depending on n(here n=3)
    # a = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
    # b = [4, 7, 3]
    # print(x)
    initialValues=[]
    a = inputToMatrix(3, equations)
    listA = [None] * n
    # print(listA.__len__())
    listLength = listA.__len__()
    l = 0
    while l < n:
        listA[l] = []
        l += 1
    # print(listA)
    index2 = 0
    oldX = []
    flag = True
    # loop run for m times depending on m the error value
    # here we specify the number of iteration
    for i in range(0, numOfIterations):
        x = seidel(a, x)
        print(x)
        for k in range(len(x)):
            output.append("%f\t" % x[k])
        k = 0
        relativeEr = []
        for j in x:
            if not flag:
                error = abs((x[k] - oldX[k]) / x[k])
                relativeEr.append(error)
            # print(k)
            # list[k][index2]=[]
            listA[k].append([i, j])
            k += 1
        index2 = index2 + 1

        # print each time the updated solution
        # print(x)



        if not flag:
            print(relativeEr)
            for k in range(len(x)):
                output.append("%f\t" % relativeEr[k])
        oldX = copy.deepcopy(x)

        relErFlag=True
        if not flag:
            for value in relativeEr:
                if value > epsilon:
                    print(value)
                    relErFlag=False

        if relErFlag and not flag:
            print("gwa if ")
            break
        flag = False

    # print(list)
    print(output)
    obj = plot.plot(listA)
    obj.draw2()


function(equations, 3, 5,0.1,x)
