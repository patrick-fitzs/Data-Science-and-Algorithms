def matrixMaker(n):
    matrix = []
    for i in range(n):
        matrix.append([0]*n)
    return matrix
# result of the function
result = matrixMaker(5)

print('initial matrix')
for row in result:
    print(row)

for i in range(len(result)):
    for j in range(len(result[i])):
        if j%2==0:
            result[i][j]+=7

print('second matrix')
for row in result:
    print(row)