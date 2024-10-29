'''
a = list
n = number of items in a
i = index to remove value at
'''

def my_remove(a,n,i):
    for j in range(i,n-1):
        a[j] = a[j+1]
        print("Value", a[j], "copied from index", j, "to", j + 1)
    a[n-1] = 0

a = [10, 20, 30, 40, 50, 0, 0]
n = 5
i = 2
my_remove(a, n, i)
print("Should have moved values 50 and 40 (in that order) into the previous slot, and then put 0 at index 4")
print(a, "should now be [10, 20, 40, 50, 0, 0, 0]")
print(len(a), "should still be 7")

a = [1, 2, 3, 4, 5, 6, 7, 0]
n = 7
i = 6
my_remove(a, n, i)
print("Should just put 0 at index 6")
print(a, "should now be [1, 2, 3, 4, 5, 6, 0, 0]")
print(len(a), "should still be 8")

a = [1, 2, 3, 4, 5, 6, 7, 0]
n = 7
i = 0
my_remove(a, n, i)
print("Should move each entry from 7 down to 2, into the previous slot, and then put 0 at index 6")
print(a, "should now be [2, 3, 4, 5, 6, 0, 0, 0]")
print(len(a), "should still be 8")

a = [1, 0, 0, 0, 0]
n = 1
i = 0
my_remove(a, n, i)
print("Should put 0 at index 0")
print(a, "should now be [0, 0, 0, 0, 0]")
print(len(a), "should still be 5")