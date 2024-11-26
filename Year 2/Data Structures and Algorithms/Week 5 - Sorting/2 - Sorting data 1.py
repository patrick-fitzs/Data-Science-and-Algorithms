

def show(list):
  print("\n".join(map(str, list)))
  print()

table = [
  [500, "John", "Smith",
      50, 45, 70],
  [321, "Arnold", "Black",
      55, 80, 60],
  [112, "Adam", "Smith",
      80, 40, 20],
  [440, "Jack", "Black",
      60, 40, 50]
]
print("Original table:")
show(table)

# Example: Sort by first name, in reverse order
print("Example: Sort by first name, in reverse order:")
def fname(record):
  return record[1]
by_fnamerev = sorted(table, key=fname, reverse=True)
show(by_fnamerev)

print("Sort by last name:")
# As above
def lname(record):
    return record[2]
by_lname = sorted(table, key=lname)
show(by_lname)

print("Sort by student id:")
# Do you need to use a key?
by_id = sorted(table)
show(by_id)

# Sort by first name in reverse alphabetical order, and then by last name in reverse order
print("Sort by first name in reverse, then by last name:")
# Can you use the previous variables?
def fname_lname(record):
    return (record[1], record[2])

by_fnamerev_lname = sorted(table, key= fname_lname, reverse=True)
show(by_fnamerev_lname)

# Sort by score on first test, then by score on second test, then by score on third test
print("Sort by each score in turn:")
def sortTest(record):
    return (record[3], record[4], record[5])
by_scores = sorted(table, key=sortTest)
show(by_scores)

print("Sort by total score:")
def totalScore(record):
    return record[3]+record[4]+record[5]
by_totalscore = sorted(table, key=totalScore, reverse=True)
show(by_totalscore)

print("Sort by first name and then by total score:")
def fname_score(record):
    return fname(record), totalScore(record)
by_fname_totalscore = sorted(table, key=fname_score)
show(by_fname_totalscore)