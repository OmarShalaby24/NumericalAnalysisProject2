import eq_mat as matrix

numberOfVariables = 3

# if a variable does not exists in equation it should bew multiplied by zero
#   x+2y=0 => x+2y+0z=0

eq = ["-6x+5y+1z=6", "x+y+z=1", "x+2y+0z=0"]
eq1 = "-6.2x+5y+1z-6.4,x+.3y+z-1,x+2y+0z-0"
Matrix = matrix.equationToMatrix(numberOfVariables, eq)
print(Matrix)
Matrix = matrix.inputToMatrix(numberOfVariables, eq1)
print(Matrix)
