"""Implement a function find_all(M, v)
taking a matrix M and a number v,
and returning a list of lists [[i1, j1], [i2, j2], ...]
giving the co-ordinates of all occurrences of v in the matrix.
If there are none, return an empty list this time.
As before, the search should proceed from the first row onwards,
and check each row from beginning to end.
(Do not check more entries than necessary!)
"""

# M being matrix
# v being the number were looking for
def find_all(M,v):
    list_with_v = []

    for i in range(len(M)):

        for j in range(len(M[i])):
            if(M[i][j]) == v:
                list_with_v.append([i,j])
    return list_with_v

M = [[1, 1], [1, 1]]
print(find_all(M, 1), "should be", [[0, 0], [0, 1], [1, 0], [1, 1]])

M = [[1, 2], [2, 1]]
print(find_all(M, 2), "should be", [[0, 1], [1, 0]])

M = [[1, 2], [3, 4], [5, 6]]
print(find_all(M, 5), "should be", [[2, 0]])

M = [[1, 2, 3], [4, 5, 6]]
print(find_all(M, 7), "should be", [])

M = [[1]]
print(find_all(M, 2), "should be", [])

