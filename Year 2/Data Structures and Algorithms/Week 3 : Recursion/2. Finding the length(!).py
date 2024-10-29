x = [1,2]
def rec_len(x):
    if x == []:
        return 0
    else:
        return 1+ rec_len(x[1:])


print(rec_len(x))
