"""Implement a function clone_mat(M) that takes a matrix M
and returns a matrix that resembles M exactly,
without any aliasing.
"""

def clone_mat(M):
    cloned = []
    for row in M:
        # Iterate through row and append a copy, not reference
        cloned.append(row[:])
    return cloned

M = [[1]]
N = clone_mat(M)
print(N, "should be", [[1]])
M[0][0] += 1
print(M, "should be", [[2]])
print(N, "should still be", [[1]])

M = [[1, 2, 3], [4, 5, 6]]
N = clone_mat(M)
print(N, "should be", [[1, 2, 3], [4, 5, 6]])
M[0][1] = 12
M[1][0] = 14
print(M, "should be", [[1, 12, 3], [14, 5, 6]])
print(N, "should still be", [[1, 2, 3], [4, 5, 6]])
