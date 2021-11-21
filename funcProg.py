# Functional Programming

# Rules of "Pure Functions"
#
# 1. Given the same input, always return the same output
# 2. Function should not produce any side effects (outside of function)
#
# So its impossible have pure functions everywhere, but when you can its better.

my_list = [12, 23, 36]
another_list = [3, 6, 15]


def multiply_by3(item):
    return item*3


def only_even(num):
    return num % 2 == 0


result = list(filter(only_even, my_list))
print(result)
print(list(map(multiply_by3, my_list)))
print(list(map(multiply_by3, another_list)))
