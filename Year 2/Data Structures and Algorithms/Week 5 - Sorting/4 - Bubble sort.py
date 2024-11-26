
# Optional functions you can use
def compare_and_swap(a, i, j):
  if a[i] > a[j]:
    swap(a, i, j)

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def bsort(x):
    n = len(x)
    for i in range(n):
        for j in range(0,n-i-1):
            if x[j]> x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x,


numbers = [1,2,3,4,5,7,5,8]

print(bsort(numbers))