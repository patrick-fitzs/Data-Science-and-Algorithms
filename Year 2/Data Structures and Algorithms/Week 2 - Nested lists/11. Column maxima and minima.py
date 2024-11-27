"""
Q11. An easy adaptation of the previous exercise:
Implement a function col_min_max(M) that returns a list of pairs [[min_0, max_0], [min_1, max_1], ...]
where min_i and max_i are the minimum/maximum values in column i of the matrix M
"""

def col_min_max(M):
    min_max_list = []

    for column in range(len(M[0])):
        currentMax = M[0][column]
        currentMin = M[0][column]

        for row in M[1:]:
            if row[column]<currentMin:
                currentMin = row[column]
            if row[column] > currentMax:
                currentMax = row[column]

        min_max_list.append([currentMin, currentMax])

    return min_max_list


M = [[6, 5, 4], [3, 4, 5], [3, 2, 1]]
print(col_min_max(M), "should be", [[3, 6], [2, 5], [1, 4]])

M = [[6], [5], [4]]
print(col_min_max(M), "should be", [[4, 6]])

M = [[6, 5, 4]]
print(col_min_max(M), "should be", [[6, 6], [5, 5], [4, 4]])

M = [[1, 2, 3], [-4, -5, -6]]
print(col_min_max(M), "should be", [[-4, 1], [-5, 2], [-6, 3]])

M = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
print(col_min_max(M), "should be", [[1, 3], [1, 3], [1, 3], [1, 3]])

M = [[9]]
print(col_min_max(M), "should be", [[9, 9]])
