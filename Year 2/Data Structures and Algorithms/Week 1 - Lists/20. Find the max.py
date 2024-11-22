'''Implement a function my_max(x) that returns the maximum value in a non-empty list of numbers x.
Do not use the built-in max function!
The most natural approach is to loop through the list,
and use a variable (e.g. max) to keep track of the largest element seen,
updating it when necessary.
One can initialise this variable to be the first number in the list, x[0],
and then loop through the remaining numbers after the first.
(Alternatively, you can initialise the variable to a “sentinel value” such as None, before looping through the whole list.
I would not use -1 as the sentinel value, because the list could contain negative numbers.)'''

def my_max(x):
    # set the max to 0
    max = 0
    # iterate through x(argument)
    for v in x:
        # if current is bigger than max, replace max, else move on to next
        if v>max:
            max = v
    return max

x = [1, 2, 3]
print(my_max(x), "should be 3")

x = [1, 2, -3]
print(my_max(x), "should be 2")

x = [3, 2, 1]
print(my_max(x), "should be 3")

x = [5]
print(my_max(x), "should be 5")

