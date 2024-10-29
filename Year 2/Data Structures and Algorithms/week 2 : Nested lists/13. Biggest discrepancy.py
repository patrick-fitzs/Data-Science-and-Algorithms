def big_discrep(M,N):
    new_list = []  # co-ords where the discrepancy occurs
    biggest_diff = 0
    for i in range(len(M)):  # Loops through the rows
        for j in range(len(M[i])):  # Loops through the columns of the current row, eg M[0][1],M[0][2],M[0][3] etc
            diff = abs(M[i][j] - N[i][j])  # Calculate the diff between the elements

            if diff > biggest_diff:
                biggest_diff = diff
                new_list = [i,j]

    return [biggest_diff, new_list]


M = [[1, 2, 3],[3, 2, 1]]
N = [[2, 4, 6], [9, 6, 3]]
print(big_discrep(M, N), "should be", [6, [1, 0]])
print(big_discrep(N, M), "should also be", [6, [1, 0]])

M = [[1, 2, 3, 4, 5, 6]]
N = [[-1, -2, -3, -4, -5, -6]]
print(big_discrep(M, N), "should be", [12, [0, 5]])
print(big_discrep(N, M), "should also be", [12, [0, 5]])

M = [[1, 2], [3, 4], [5, 6]]
N = [[-1, -2], [-3, -4], [-5, -6]]
print(big_discrep(M, N), "should be", [12, [2, 1]])
print(big_discrep(N, M), "should also be", [12, [2, 1]])

M = [[5]]
N = [[12]]
print(big_discrep(M, N), "should be", [7, [0, 0]])