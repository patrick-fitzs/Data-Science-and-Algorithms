def rec_addlists(x, y):
    # if both are empty, return an empty list
    if x == [] and y == []:
        return []
    else:
        # first index is x[0]+y[0]
        head_sum = x[0] + y[0]
        # now add next[0]+[0] through function and add to call stack
        tail_sum = rec_addlists(x[1:], y[1:])
        # unwind stack and add results to one list(head sum)
        return [head_sum] + tail_sum

def rec_addmats(M, N):
    if M == [] and N == []:
        return []
    else:
        # Add the first rows of M and N
        p_sum = rec_addlists(M[0], N[0])
        # Recursively add the remaining rows through addmats
        # which calls the first indexes with add lists again
        p_tail = rec_addmats(M[1:], N[1:])
        # combine the head and tail results
        return [p_sum] + p_tail

M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

N = [[9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]
P = rec_addmats(M, N)

print(P)
