import eq_mat as matrix

numberOfVariables = 3
eq = ["5x+3y+6z=5","6x+5y+1z=6","x+y+z=1"]
Matrix = matrix.equationToMatrix(numberOfVariables,eq)
print(Matrix)
