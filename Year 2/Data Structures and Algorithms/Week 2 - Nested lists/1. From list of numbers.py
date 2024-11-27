""" From list of numbers
In the top-left tab, implement a function list_to_mat(x, m, n)
taking a list of numbers x,
and two numbers n, m.
It should return an m x n matrix with m rows and n columns, containing the elements in x.
You can assume x contains the correct number of items (n * m)."""


def list_to_mat(x,m,n):
    # create new matrix
    new_matrix=[]
    # iterate over m(2) so 0,1
    for i in range(m):
        # row = position[0*2:0+1*2==3]
        row = x[i*n: (i+1)*n]
        # append and enter second and last iteration
        new_matrix.append(row)
    return new_matrix

# Below is teachers explanation, however it doesnt make use of the parameters
# def list_to_mat(x,m,n):
#     #initiate matrix and a row
#     matrix = []
#     row = []
#     # iterate through elements in x which is the list
#     for v in x:
#         # start adding v to new row
#         row.append(v)
#         # if the length of this row is n(length of the column)
#         if len(row) == n:
#             # add to the martin
#             matrix.append(row)
#             # clean the row and continue with "for v in x"
#             row = []
#     return matrix

M = list_to_mat([1, 2, 3, 4], 2, 2)
print(M, "should be", [[1, 2], [3, 4]])

M = list_to_mat([1, 2, 3, 4, 5, 6], 2, 3)
print(M, "should be", [[1, 2, 3], [4, 5, 6]])

M = list_to_mat([1, 2, 3, 4, 5, 6], 3, 2)
print(M, "should be", [[1, 2], [3, 4], [5, 6]])

M = list_to_mat([1, 2, 3, 4, 5, 6], 6, 1)
print(M, "should be", [[1], [2], [3], [4], [5], [6]])

M = list_to_mat([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
print(M, "should be", [[1, 2, 3], [4, 5, 6], [7, 8, 9]])



