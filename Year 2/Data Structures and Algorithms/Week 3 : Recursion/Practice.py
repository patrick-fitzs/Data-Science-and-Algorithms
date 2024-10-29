

def sum(x):
    if x ==[]:
        return 0
    else:
        head =x[0]
        tail = x[1:]
        tail_sum = sum(tail)
        return head + tail_sum

x = [1,2,3,4,5,19]
y = list(range(1,101))
print(sum(y))
print(sum(x))