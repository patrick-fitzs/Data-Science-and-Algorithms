'''Matrix of zeroes
In the top-left tab,
implement a function zero_mat(n) that takes one number n and returns a square matrix with n rows and n columns,
all of which should contain zeroes.
There should be no aliasing;
changing one entry should not change any others.'''

# n is length of rows and columns

def zero_mat(n):
    # make empty matrix
    matrix = []
    for i in range(n):
        # iterate 0, [0]*2 = [0,0]
        # iterate 1, [0]*2 = [0,0]
        # iteration stops
        matrix.append([0]*n)
    return matrix

M = zero_mat(2)
print(M, "should be", [[0, 0], [0, 0]])
M[0][0] = 1
print(M, "should be", [[1, 0], [0, 0]])
M[1][1] = 2
print(M, "should be", [[1, 0], [0, 2]])


M = zero_mat(3)
print(M, "should be", [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
M[0][0] = 1
print(M, "should be", [[1, 0, 0], [0, 0, 0], [0, 0, 0]])
M[1][1] = 2
print(M, "should be", [[1, 0, 0], [0, 2, 0], [0, 0, 0]])
M[2][2] = 3
print(M, "should be", [[1, 0, 0], [0, 2, 0], [0, 0, 3]])

M = zero_mat(1)
print(M, "should be", [[0]])