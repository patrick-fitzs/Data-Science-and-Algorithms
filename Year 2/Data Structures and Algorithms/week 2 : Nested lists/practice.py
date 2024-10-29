M = [[6, 5, 4],
     [3, 4, 5],
     [3, 2, 1]]

for col_index in range(len(M[0])):
    print(f"Column {col_index}:")
    for row in M:
        print(row[col_index])
