'''Implement the function listind_to_mat(l, m, n)
taking a list l consisting of m lists,
one for each row, where these lists contain only numbers 0...n-1,
 column indices. It should return a matrix M of size m x n,
 whose entries are all 0,
 except for the ones whose indices are identified by l, which have value 1.
 See below:'''

# l is the list
# m number of lists in l, (rows)
# n columns
def listind_to_mat(l,m,n):
    matrix = []
    for i in range(m):
        row = [0] * n
        matrix.append(row)

    for i in range(m):
        for j in l[i]:
            matrix[i][j] = 1

    return matrix


M = listind_to_mat([[0], [1], [1], [0, 1], [0]], 5, 2)
print(M, "should be", [[1, 0], [0, 1], [0, 1], [1, 1], [1, 0]])

M = listind_to_mat([[0], [1, 2], [0, 1, 2]], 3, 3)
print(M, "should be", [[1, 0, 0], [0, 1, 1], [1, 1, 1]])

M = listind_to_mat([[0, 2], [2, 3], [0, 3]], 3, 4)
print(M, "should be", [[0, 0, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]])
