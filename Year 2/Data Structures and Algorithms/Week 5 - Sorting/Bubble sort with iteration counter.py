def bubble_sort_and_count_swaps(arr):
    n = len(arr)
    swap_counter = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_counter += 1

    return arr, swap_counter

# Example usage:
sorted_arr, total_swaps = bubble_sort_and_count_swaps([5, 4, 3, 2, 1])
print(f"Sorted array: {sorted_arr}")
print(f"Total swaps: {total_swaps}")
print("tt")