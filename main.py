import eq_mat as matrix

numberOfVariables = 3

#if a variable does not exists in equation it should bew multiplied by zero
#   x+2y=0 => x+2y+0z=0

eq = ["-6x+5y+1z=6","x+y+z=1","x+2y+0z=0"]
Matrix = matrix.equationToMatrix(numberOfVariables,eq)
print(Matrix)
