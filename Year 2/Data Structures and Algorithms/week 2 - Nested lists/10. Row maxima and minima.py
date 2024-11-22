"""Implement a function row_min_max(M)
that returns a list of pairs [[min_0, max_0], [min_1, max_1], ...]
where min_i and max_i are the minimum/maximum values in row i of the matrix M.
You may find it useful to have two local variables
for tracking the minimum and maximum as you iterate through each row;
and to initialise them both to the first number in the row
(and start your search from the second item in the row onwards).
"""

def row_min_max(M):
    min_max_list = []


    for row in M:
        #  make the first elem of the row both min and max
        currentMax = row[0]
        currentMin = row[0]

        for num in row[1:]:  # start checking from the second element, first is already min and mac
            if num < currentMin:  # if current elem is less than min, make new min
                currentMin = num
            if num > currentMax:  # if current elem is bigger than max, make new max
                currentMax = num
        min_max_list.append([currentMin,currentMax])  # append the pair for the current row
    return min_max_list

M = [[6, 5, 4],
     [3, 4, 5],
     [3, 2, 1]]
print(row_min_max(M), "should be", [[4, 6], [3, 5], [1, 3]])

M = [[6], [5], [4]]
print(row_min_max(M), "should be", [[6, 6], [5, 5], [4, 4]])

M = [[6, 5, 4]]
print(row_min_max(M), "should be", [[4, 6]])

M = [[1, 2, 3], [-4, -5, -6]]
print(row_min_max(M), "should be", [[1, 3], [-6, -4]])

M = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
print(row_min_max(M), "should be", [[1, 1], [2, 2], [3, 3]])

M = [[9]]
print(row_min_max(M), "should be", [[9, 9]])