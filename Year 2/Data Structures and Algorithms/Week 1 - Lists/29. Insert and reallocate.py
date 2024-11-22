'''
a = list
x = the value to insert
n = len of list
i = index to insert at
'''

def insert_realloc(a,x,n,i):
    if n < len(a):
        for j in range(n, i, -1):
            a[j] = a[j-1]
            print("Value", a[j], "copied from index", j, "to", j + 1)
        a[i] = x
        print("Value", x, "inserted at index", i)
        return a

    else:
        new_list = [0] * (2*n)
        for j in range(n):
            new_list[j] = a[j]
            print("Value", a[j], "copied from index", j, "to", j)

        new_list[i] = x  # Insert new value
        print("Value", x, "inserted at index", i)

        return new_list  # Returning the new list


a = [0]
n = 0
x = 1
i = 0
result = insert_realloc(a, x, n, i)
print("Should put 1 at index 0")
print(result, "should be [1]")
print(result is a, "should be True")
print(len(result), "should be 1")

a = [10, 20, 40, 0]
n = 3
x = 30
i = 2
result = insert_realloc(a, x, n, i)
print("Should move values 40 into the next slot, and then put 30 at index 2")
print(result, "should be [10, 20, 30, 40]")
print(result is a, "should be True")
print(len(result), "should still be 4")

a = [10, 20, 30, 40]
n = 4
x = 5
i = 3
result = insert_realloc(a, x, n, i)
print("Should create a new array of size 8, and copy the values into it, followed by 50")
print(result, "should be [10, 20, 30, 40, 50, 0, 0, 0]")
print(result is a, "should be False")
print(len(result), "should be 8")


a = [0]
for i in range(0, 8):
  n = i
  x = i
  a = insert_realloc(a, x, n, i)
print(a, "should now be [0, 1, 2, 3, 4, 5, 6, 7]")


