def bit_strings(n):
  if n == 0:
    return []
  rest = bit_strings(n - 1)
  strings = []
  for string in rest:
    string0 = string.append(0)
    string1 = string.append(1)
    strings.append(string0)
    strings.append(string1)
  return strings

print(bit_strings(3))