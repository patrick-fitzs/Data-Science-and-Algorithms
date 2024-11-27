
"""
Implement a function mat_from_row(r, m)
that takes a list of numbers r and a positive integer m,
and returns a matrix with m rows,
all of which resemble r but are not aliases.
You can create a copy of a list r in a few ways: e.g.
by creating an empty list and appending each element of r in turn;
or using the slice r[:].
"""
def mat_from_row(r,m):
    new_martix = []
    for i in range(m):
        '''r[:] creates a shallow copy of r from start to finish
            similar to r[::] or r[:::], append(r) creates a reference copy, '''
        new_martix.append(r[:])
    return new_martix


r = [1, 10, 100]
M = mat_from_row(r, 3)
print(M, "should be", [[1, 10, 100], [1, 10, 100], [1, 10, 100]])
M[0][2] += 1
print(M, "should be", [[1, 10, 101], [1, 10, 100], [1, 10, 100]])
M[2][1] -= 1
print(M, "should be", [[1, 10, 100], [1, 10, 101], [1, 9, 100]])
print(r, "should still be", [1, 10, 100])


M = mat_from_row([1, 10, 100], 3)
print(M, "should be", [[1, 10, 100]])
M[1] = 9
print(M, "should be", [[1, 9, 100]])
print(r, "should still be", [1, 10, 100])

print("Just testing matrix row replacement")
test1 = [[1,2,3],[4,5,6],[7,8,9]]
test1[1]= 22
print(test1)



