"""Implement a function col_totals(M)
that returns a list of numbers [sum_0, sum_1, ...]
where sum_i is the sum of the values in column i of the matrix M.
"""

def col_totals(M):
    list_of_sums = [0] * len(M[0]) # list of sums, one for each column
    print(list_of_sums)

    for row in M:
        for j in range(len(row)): # iterate through each element in the row
            list_of_sums[j] +=row[j] # add the value to the appropriate column sum

    return list_of_sums


M = [[6, 5, 4],
     [3, 4, 5],
     [3, 2, 1]]
print(col_totals(M), "should be", [9, 9, 9])

M = [[6], [5], [4]]
print(col_totals(M), "should be", [15])

M = [[6, 5, 4]]
print(col_totals(M), "should be", [[6], [5], [4]])

M = [[1, 2, 3],
     [-4, -4, -4]]
print(col_totals(M), "should be", [[-3], [-2], [-1]])

M = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3]]
print(col_totals(M), "should be", [3, 3, 3, 3])

M = [[9]]
print(col_totals(M), "should be", [9])