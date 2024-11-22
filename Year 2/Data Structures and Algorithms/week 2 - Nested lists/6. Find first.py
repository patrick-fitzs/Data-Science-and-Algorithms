"""
Implement a function find_first(M, v) taking a matrix M and a number v,
and returning a list [i, j]
giving the co-ordinates of the first occurrence of v in the matrix,
at row i and column j. If it cannot be found, return None.
The search should proceed from the first row onwards,
and check each row from beginning to end.
(Do not check more entries than necessary!)
"""

# M is the matrix
# V is a number

def find_first(M,v):
    # iterate throught M
    for i in range(len(M)):
# nested iteration in m, so iterates through the list in the list M
        for j in range(len(M[i])):
            # if value at index M([0][0]) == v/// return
            if (M[i][j]) == v:
                return [i,j]
    return None

M = [[1, 1], [1, 1]]
print(find_first(M, 1), "should be", [0, 0])

M = [[1, 2], [2, 1]]
print(find_first(M, 2), "should be", [0, 1])

M = [[1, 2], [3, 4], [5, 6]]
print(find_first(M, 5), "should be", [2, 0])

M = [[1, 2, 3], [4, 5, 6]]
print(find_first(M, 7), "should be", None)

M = [[1]]
print(find_first(M, 2), "should be", None)