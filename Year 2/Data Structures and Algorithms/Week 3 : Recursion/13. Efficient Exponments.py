def rec_pow(x,n):
    # any number by the power of 0 is 1
    if n == 0:
        return 1
    else:
        # return x n0 is 1
        # n1 is 3*1, return 3,
        # n2 is returned 3*3 9,
        # n3 is 3*9 (3*3*3) 27 and so on
        return x*rec_pow(x,n-1)

print(rec_pow(3,9))
