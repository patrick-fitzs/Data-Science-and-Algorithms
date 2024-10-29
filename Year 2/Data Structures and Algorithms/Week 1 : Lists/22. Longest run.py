'''Implement a function longest_run(x) that,
given a non-empty list of numbers x,
returns the length of the longest section where only one value is repeated (a “run”).
Hint: You may find it helpful to adapt your previous code for immed_reps,
by introducing another variable to track the length of the longest run seen so far,
and resetting the other variable when a new element is encountered. '''

def longest_run(x):
    '''initiate current and longest run at 1'''
    current_run = 1
    longestRun= 1
    '''iterate throught the range ox x, starting at index1 -len'''
    for i in range(1, len(x)):
        '''if current index == prev'''
        if x[i] == x[i - 1]:
            '''bump up the current run by one '''
            current_run += 1
            '''if not ... below'''
        else:
            '''now check if the current run is longer, if yes, store it and reset current run'''
            if current_run > longestRun:
                longestRun = current_run
            current_run = 1

    if current_run > longestRun:
        longestRun = current_run
    return longestRun



x = [2, 2, 2, 1, 1, 0]
print(longest_run(x), "should be 3")

x = [2, 1, 1, 1, 1, 3, 3]
print(longest_run(x), "should be 4")

x = [3, 1, 4, 1, 5, 5]
print(longest_run(x), "should be 2")

x = [2, 3, 2, 3, 2]
print(longest_run(x), "should be 1")

x = [5]
print(longest_run(x), "should be 1")