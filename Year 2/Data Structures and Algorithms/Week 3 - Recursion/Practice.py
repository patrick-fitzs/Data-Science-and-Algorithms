x = [1,2,3,4,5]
def sum_list(x):
    if x == []:
        return 0
    else:
        head = x[0]
        tail = x[1:]

    return head+sum_list(tail)

print(sum_list(x))
