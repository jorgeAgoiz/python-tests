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
# my_list = [5, 4, 3]

# print(list(map(lambda item: item**2, my_list)))


# a = [(0, 2), (4, 3), (9, 9), (10, -1)]


# def printSecond(item):
#     return item[1]


# print(list(map(printSecond, a)))

# list comprehension

# my_list_name = [char for char in "hello my name is Jorge"]
# my_list_two = [num for num in range(0, 100)]
# my_list_three = [num**2 for num in range(0, 100)]
# my_list_four = [num**2 for num in range(0, 100) if num % 2 == 0]

# print(my_list_name)
# print(my_list_two)
# print(my_list_three)
# print(my_list_four)

# EXERCISE

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = set([char for char in some_list if some_list.count(
#     char) > 1])

# print(duplicates)

# DECORATORS

# def my_decorator(f):
#     def wrapper_function(*args):
#         print("Calculating...")
#         f(*args)
#         print("Calculated!!")
#     return wrapper_function


# @my_decorator
# def suma(a, b):
#     return print(a+b)


# @my_decorator
# def resta(a, b):
#     return print(a-b)


# @my_decorator
# def multiply(a, b):
#     return print(a*b)


# @my_decorator
# def division(a, b):
#     return print(a/b)


# suma(12, 6)
# resta(23, 12)
# multiply(2, 36)
# division(12, 3)
print(__name__)
