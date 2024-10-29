def rec_oddsum(x):
    if x == []:
        return 0
    else:
        head = x[0] if x[0] % 2 == 1 else 0
        tail = x[1:]
    return head + rec_oddsum(tail)


y = [1, 2, 3, 4, 5, 6]  # Odd numbers : 1,3,5 = 9
print(rec_oddsum(y))

#  below is another way
def rec_oddsum(x):
    # Base case: if the list is empty, return 0
    if x == []:
        return 0
    else:
        head = x[0]
        tail = x[1:]

        # Check if the head is odd
        if head % 2 == 1:
            # If the head is odd, add it to the sum of the tail
            return head + rec_oddsum(tail)
        else:
            # If the head is even, skip it and sum the tail
            return rec_oddsum(tail)