def pascal(n):
    if n == 0:
        return [1]
    elif n ==1:
        return [1,1]
    else:
        previous_row = pascal(n-1)
        current_row = [1]
        for i in range(1,len(previous_row)):
            current_row.append(previous_row[i-1] + previous_row[i])
        current_row.append(1)
        return current_row

print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
