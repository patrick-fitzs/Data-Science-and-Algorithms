def isort(x):
  n = len(x)
  swap_count = 0
  for i in range(1, n):
    swap_count +=put_in_place(x, i)

  print(f"swap count: {swap_count}")

def put_in_place(x, i):
  value = x[i]
  swaps = 0
  while i > 0 and x[i - 1] > value:
    x[i] = x[i - 1]  # Move other values forward
    i-=1
    swaps += 1
  x[i] = value       # Insert at right place
  return swaps

# For question 4

# Optional -- you don't have to use this function:
def put_in_place_view(x, i, begin):
  """YCH"""

def isort_view(x, begin, end):
  """YCH"""

arr = [5, 3, 4, 1, 2]


arr = [6, 1, 7, 4, 2, 9, 8, 5, 3]
arr = [6, 1, 7, 7, 2, 9, 8, 5, 3]


x = ["e", "d", "c", "b", "a"]



def insertionSort(arr):

    for i in range(1, len(arr)):
        # store the current element starting from the second element
        temp = arr[i]
        # initialise pointer called j which is i-1 / last index sorted
        j = i-1
        print(j) # current value of j
        print(f"arr before", arr) # show array before any changes

        # while j is greater/equal than 0 index and temp[i] is less than j(i-1)(elem before it)
        while j >=0 and temp < arr[j]:
            print(f"is [{temp}] less than [{arr[j]}]")
            print("Swap elements")
            print(f"this [{arr[j+1]}] new equals [{arr[j]}]")
            # swap larger element to the right. j is now j+1
            arr[j+1] = arr[j]
            print(f"store i with i-1, {arr}")
            j-=1 # move pointer one step left
        arr[j+1] = temp
        print(f"arr after swap", arr)
    return arr


print(insertionSort(x))
