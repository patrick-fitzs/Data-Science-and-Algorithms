# # x = [8,3,9,7,1]
# #
# # n = len(x)
# # for i in range(n):
# #     print(f"index {i} contains number {x[i]}")
# #
# # for i,value in enumerate(x):
# #     print(f"Using enumeration, the values at index {i} are {value}")
#
# # new_list = n *[0]
# a = [10, 20, 40, 50, 60, 0, 0, 0]
# n = 5
# x = 3
# i = 2
#
# # insert value x into the list a st position i
# # n is just the length of the array
# def myInserter(a,x,n,i):
#     for j in range(n-1)


def FizzBuzz(x):
    if x%3==0 and x%5==0:
        return "Fizzbuzz"
    if x%3==0:
        return "Fizz"
    if x%5==0:
        return "Buzz"
    else:
        return "Welp"

print(FizzBuzz(15))