x = [1,2]
def rec_len(x):
    if x == []:
        return 0
    else:
        return 1+ rec_len(x[1:])


print(rec_len(x))

# Lecturer solution below
def rec_len(x):
  if x == []:
    return 0
  tail = x[1:]
  tail_len = rec_len(tail)
  return tail_len + 1

