def rec_flatten(M):
    if M == []: # same as "if not M"
        return []
    else:
        head = M[0]
        tail = M[1:]
        return head + rec_flatten(tail)

M1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(f"Input: {M1} -> Flattened: {rec_flatten(M1)}")