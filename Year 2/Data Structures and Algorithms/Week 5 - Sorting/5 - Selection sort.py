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
