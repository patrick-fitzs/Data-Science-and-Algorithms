def rec_reps(x):
    if x == []:
        return 0
    else:
        head = x[0]
        tail = x[1:]
        if tail and head == tail[0]:
            return 1+ rec_reps(tail)
        else:
            return rec_reps(tail)

example_list_1 = [1, 1, 2, 2, 2, 3, 3, 4]
print(f"Input: {example_list_1} -> Consecutive repeats: {rec_reps(example_list_1)}")
