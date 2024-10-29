'''Implement a function immed_reps(x) that,
given a list of numbers x,
counts how many times an element is the same as the previous one.
'''

def immed_reps(x):
    counter = 0
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            counter += 1
    return counter

x = [3, 3, 3]
print(immed_reps(x), "should be 2")

x = [1, 3, 3, 3, 3, 3]
print(immed_reps(x), "should be 4")

x = [3, 3, 1, 4, 4, 1, 5, 5]
print(immed_reps(x), "should be 3")

x = [1, 2, 1, 3, 1, 4]
print(immed_reps(x), "should be 0")

x = [5]
print(immed_reps(x), "should be 0")

x = []
print(immed_reps(x), "should be 0")