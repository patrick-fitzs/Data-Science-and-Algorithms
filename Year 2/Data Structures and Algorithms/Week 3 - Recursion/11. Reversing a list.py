def rec_rev(x):
    if x == []:
        return []
    else:
        head = x[0]
        tail = x[1:]
        # recursively reverse the tail and add the head this time (doing it backwards)
        return rec_rev(tail) + [head]
        # return [head] + rec_rev(tail)

y = [1,2,3,4]
print(rec_rev(y))