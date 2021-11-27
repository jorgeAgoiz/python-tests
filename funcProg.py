# Functional Programming

# Rules of "Pure Functions"
#
# 1. Given the same input, always return the same output
# 2. Function should not produce any side effects (outside of function)
#
# So its impossible have pure functions everywhere, but when you can its better.

# my_list = [12, 23, 36]
# another_list = [3, 6, 15]


# def multiply_by3(item):
#     return item*3


# def only_even(num):
#     return num % 2 == 0


# result = list(filter(only_even, my_list))
# print(result)
# print(list(map(multiply_by3, my_list)))
# print(list(map(multiply_by3, another_list)))
# print(list(zip(my_list, another_list)))

# First exercise
my_list = [5, 4, 3]

print(list(map(lambda item: item**2, my_list)))


a = [(0, 2), (4, 3), (9, 9), (10, -1)]


def printSecond(item):
    return item[1]


print(list(map(printSecond, a)))
