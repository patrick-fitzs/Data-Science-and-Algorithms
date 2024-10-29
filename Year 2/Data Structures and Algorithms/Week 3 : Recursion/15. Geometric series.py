def geomseries(x):
    if len(x) == 1:
        return x[0]
    else:
        head = x[0]
        tail = x[1:]
        return head * (1+geomseries(tail))


list = ["a","ab","abc","abcd","abcde"]
num_list = [1,2,3,4]
print(geomseries(num_list))