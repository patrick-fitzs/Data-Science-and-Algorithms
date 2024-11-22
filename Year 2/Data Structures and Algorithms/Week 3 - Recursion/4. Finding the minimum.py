def rec_min(x):
    #  Base case, if one elem in list, return that elem as it is obviously the smallest
    if len(x) == 1:
        return x[0]
    else:
        #  Split to first element of the list
        head = x[0]
        #  Below is the rest of the elements
        tail = x[1:]
        #  Recursive call is to find the minimum
        min = rec_min(tail)

        #  Return the min
    return head if head < min else min


x = [3, 2, 7, 9]
print(rec_min(x))

#  A shorter return statement
# def rec_min(x):
#     if x == []:
#         return float('inf')
#     else:
# // directly compare head with the recursive call on the tail
#  RETURN X[0] IF X[0] < REC_MIN(X[1:]) ELSE REC_MIN(X[1:])
