# Example

def size(z):
  return "This is the absolute value" + abs(z) # Absolute value function

# Takes a
def sort_size(x):
  return "This sorts the list using size function as the key "+ sorted(x, key=size)

# If preferred, you can also arrange it like this:
def sort_size(x):
  def size(z): # A "local function" that can only be used within sort_size
    return abs(z)
  return sorted(x, key=size)

# Lastly, this also works:
def sort_size(x):
  return sorted(x, key=abs)

# Question 1

def fraction_value(list):
  a,b = list
  return a/b

def sort_frac(x):
  return sorted(x, key=fraction_value)

print(sort_frac([[1, 2], [2, 5], [1, 3], [1, 4]]), "should be", [[1, 4], [1, 3], [2, 5], [1, 2]])

# Question 2

def maxlist(list):
  return max(list)
def sort_max(x):
  return sorted(x, key= maxlist)
print("Sort_max --> ", sort_max([[3, 1], [2], [1, 1, 5], [2, 4]]), "should be", [[2], [3, 1], [2, 4], [1, 1, 5]])

# Question 3
def word_count(s):
  return len(s.split())
def sort_count(x):
  return sorted(x,key=word_count)
print("\nThis sorts by letter count --> \n", sort_count(["bat man", "ant", "aardvark r us"]), "should be", ["ant", "bat man", "aardvark r us"])

# Question 4
def vowel_count(words):
  count = 0
  for char in words:
    if char in "aeiou":
      count+=1
  return count


def sort_vowel(x):
  return sorted(x, key= vowel_count)

print("\nThis sorted by vowel count -->\n", sort_vowel(["octopus", "to", "teepee", "doe"]), "should be", ["to", "doe", "octopus", "teepee"])

# Question 5
def biggest(rows):
  return rows[0]
def sort_rowfirst(x):
  return sorted(x, key=biggest)

print("\nThis sorts a matrix by its first entry in row[0] -->\n", sort_rowfirst([[9, 1, 1], [50, 0, 0], [1, 1, 8]]), "should be", [[1, 1, 8], [9, 1, 1], [50, 0, 0]])

# Question 6

def sum_row(rows):
  return sum(rows)
def sort_rowsum(x):
  return sorted(x, key= sum_row)

print("\nThis sorts rows by their sum-->\n", sort_rowsum([[9, 1, 1], [50, -50, 9], [1, 1, 8]]), "should be", [[50, -50, 9], [1, 1, 8], [9, 1, 1]])

