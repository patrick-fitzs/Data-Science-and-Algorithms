"""Implement a function ind_nonzero_row(M)
taking a matrix M and returning a list of lists [nz_0, nz_1, ...]
where nz_i gives the indices of all the non-zero values in row i.
(If row i only consists of zeros, then nz_i should be the empty list.)
"""


def ind_nonzero_row(M):
    # list to store non-empty 0's for each row
    list_of_zeros = []

    for i in range(len(M)):  # iterate over each row
        nonZero_Indices = []  # list to store non zero indices for current row
        for j in range(len(M[i])): #  Iterate over each element in the row
            if M[i][j] != 0:  # if element j in current column is not 0,
                nonZero_Indices.append(j)  # append column index
        list_of_zeros.append(nonZero_Indices)  # append this list of non zero indices for this row

    return list_of_zeros  # return the final list of lists


M = [[0, 0, 5], [0, 7, 0]]
print(ind_nonzero_row(M), "should be", [[2], [1]])

M = [[0, 5, 6], [7, 8, 0]]
print(ind_nonzero_row(M), "should be", [[1, 2], [0, 1]])

M = [[0, 0, 3], [0, 3, 0], [3, 0, 0]]
print(ind_nonzero_row(M), "should be", [[2], [1], [0]])

M = [[0, 0, 0], [3, 2, 1], [0, 0, 0]]
print(ind_nonzero_row(M), "should be", [[], [0, 1, 2], []])

M = [[0]]
print(ind_nonzero_row(M), "should be", [[]])

M = [[9]]
print(ind_nonzero_row(M), "should be", [[0]])
