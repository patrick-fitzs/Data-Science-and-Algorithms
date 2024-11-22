'''Implement a function records(x) that accepts a non-empty list of numbers x;
goes through each element from beginning to end;
and returns the count n of elements that are “record highs” – bigger than all previous elements.
We can consider the first number to be a record high too.
Hint: You can adapt your code for finding the maximum, this time using two variables:
one to keep track of the largest element so far, and another to count the number of records.'''

# iterate through the list
# check if x[i] > x[i-1]
# if yes
#     increment counter
# return counter

def records(x):
    # counter starts at 1 (Considered a record high)
    counter = 1
    for i in range(1,len(x)):
        if x[i] > x[i-1]:
            counter+=1
    return counter

x = [4, 3, 2, 1]
print(records(x), "should be 1")

x = [2, 4, 3, 2, 1]
print(records(x), "should be 2")

x = [2, 3, 4, 3, 2, 1]
print(records(x), "should be 3")

x = [1, 2, 3, 4]
print(records(x), "should be 4")

x = [5]
print(records(x), "should be 1")