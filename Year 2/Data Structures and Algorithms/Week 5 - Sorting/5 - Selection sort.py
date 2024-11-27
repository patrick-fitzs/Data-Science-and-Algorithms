def selection_sort(arr):
    n = len(arr)
    swap_counter = 0
    for i in range(n):
        min_index = i
        # pretend first is smallest
        for j in range(i+1, n):
            # iterate and compare i with i+1
            if arr[j]<arr[min_index]:
                # if i+1 < i
                min_index = j
        if min_index!=i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swap_counter+=1

    return arr, swap_counter

y = [5,4,3,2,1]
print(selection_sort(y))


'''
From codio
'''
# x = list

def swap(x, i, j):
    if i!=j: # This stops any unnecessary swaps
        x[i], x[j] = x[j], x[i]

def find_max(x, end):
  max_index = 0
  for i in range(1,end+1):
      if x[i] > x[max_index]:
          max_index = i
  return max_index
  #"""Return index of maximum element between x[0] and x[end] inclusive"""

def ssort(x):
  n = len(x)
  for i in range(n - 1, -1, -1):
    max_index = find_max(x, i)
    swap(x, i, max_index)

x = [2, 6, 3, 5, 1, 4]
ssort(x)
print(x, "should be", [1, 2, 3, 4, 5, 6])

#######################################

def find_min(x, begin):
  """Return index of minimum element from x[begin] to x[-1] inclusive"""
  min_index = begin
  for i in range(begin+1,len(x)):
      if x[i] < x[min_index]:
          min_index = i
  return min_index

def ssort_op(x):
  """YCH"""
  n = len(x)
  for i in range(n):
      min_index = find_min(x, i)
      swap(x, i, min_index)

x = [2, 6, 3, 5, 1, 4]
ssort_op(x)
print(x)  # Output should be [1, 2, 3, 4, 5, 6]

