# as A matrix, Solution and B matrix
from eq_mat import inputToMatrix
equations="4x+1y+2z-4,3x+5y+1z-7,1x+1y+3z-3"
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


# int(input())input as number of variable to be solved
# n is the number of equations
n = 3
#a = []
#b = []
# initial solution depending on n(here n=3)
x = [0, 0, 0]
#a = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
#b = [4, 7, 3]
#print(x)
a=inputToMatrix(3,equations)
# loop run for m times depending on m the error value
# here we specify the number of iteration
for i in range(0, 5):
    x = seidel(a, x)
    # print each time the updated solution
    print(x)
