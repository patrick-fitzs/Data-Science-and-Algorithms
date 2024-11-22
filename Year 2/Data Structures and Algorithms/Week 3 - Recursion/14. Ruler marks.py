def rec_ruler(n):
    if n == 1:
        return [1]
    else:
        # return list plus n plus list, this matches pattern backwards
        return rec_ruler(n-1) + [n] + rec_ruler(n-1)

print(rec_ruler(4))

'''
Pattern below
n = 1: Just [1].
n = 2: [1, 2, 1].
n = 3: [1, 2, 1, 3, 1, 2, 1].
n = 4: [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1].
'''