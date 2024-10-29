def rec_prod(x):
    if x == []:
        return 1
    else:
        head = x[0]
        tail = x[1:]

        return head * rec_prod(tail)


x = [1,2,3,4,5]
print(rec_prod(x))
