'''
Implement a function get_from_rows(M, ids)
that takes a matrix M and a list of indexes ids.
It should return a list containing:
The value in the first row with index ids[0] (seeing the row as a list);
The value in the second row with index ids[1];
…And so on.
You can assume none of these indices are out of bounds.
'''

def get_from_rows(M, idx):
    new_list = []

    for i in range(len(idx)):
        new_list.append(M[i][idx[i]])

    return new_list


M = [[6, 5, 4],
     [3, 4, 5],
     [3, 2, 1]]
print(get_from_rows(M, [0, 1, 2]), "should be", [6, 4, 1])

M = [[1, 5], [5, 2], [3, 5]]
print(get_from_rows(M, [0, 1, 0]), "should be", [[1, 2, 3]])

M = [[6, 5, 4]]
print(get_from_rows(M, [2]), "should be", [4])

M = [[6], [5], [4]]
print(get_from_rows(M, [0, 0, 0]), "should be", [6, 5, 4])

M = [[9]]
print(get_from_rows(M, [0]), "should be", [9])
