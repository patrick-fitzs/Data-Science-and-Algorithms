def binary_search(array, target):
    low=0
    high = len(array)-1

    while low<=high:
        mid=(low+high)//2

        if array[mid]==target:
            return mid
        elif array[mid]> target:
            high=mid-1
        else:
            low=mid+1

arr = [1,2,5,7,9,11,13,15,17,19]
target= 1

print(binary_search(arr, target))