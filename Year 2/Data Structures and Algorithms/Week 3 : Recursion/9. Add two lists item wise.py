# add two lists, item wise
# eg [2,5,7]+[2,3,1] = [4,8,8]

# 2 lists parsed into the function
def rec_addlists(x,y):
    # if both are empty, return
    if x == [] and y == []:
        return []
    else:
        # first index is x[0]+y[0]
        head_sum = x[0] + y[0]
        # now add next[0]+[0] through function and add to call stack
        tail_sum = rec_addlists(x[1:], y[1:])
        # unwind stack and add results to one list(head sum)
        return [head_sum] + tail_sum

x1 = [1, 2, 3]
y1 = [4, 5, 6]
print(f"Input: {x1}, {y1} -> Output: {rec_addlists(x1, y1)}")  # Should be [5, 7, 9]


