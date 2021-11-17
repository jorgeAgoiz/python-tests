# long_string = '''
#     !!!!!
#     0   0
#       I
#     -----
#       U
#     WELCOME TO
#     PYTHON JORGE!!!
# '''
# print(12 // 5)
# print(bin(12))
# print(long_string)
# string_test = "Hello, it's my \"pleasure\" jeje"
# print(string_test)
# name = 'Jorge'
# age = 36
# print(f'My name is {name} and I have {str(age)} years old')
# print('My name is {0} and I have {1} years old'.format(name, age))
# my_string = 'JorgeAgoizPedraja'
# print(my_string[5:10:2])
# visible = True
# print(visible)
# print('12' * 12)
# my_cars = ['citroen zx', 'seat leon',
#            'nissan 350z', 'vw golf gti', 'opel astra OPC']
# my_cars.insert(2, 'toyota corolla hybrid')
# print(my_cars)
# my_own_matrix = [
#     [1, 0, 1],
#     [0, 1, 0],
#     [1, 0, 1]
# ]
# print(my_own_matrix[0][1])
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)
# dictionary = {
#     'a': 12,
#     'b': 34
# }
# print(dictionary['a'])
# age_one = 36
# age_two = 12
# if age_one >= age_two:
#     print(
#         f"La variable age_one con el valor: {age_one}, es mayor o igual que la variable age_two con valor: {age_two}")
# else:
#     print(
#         f"La variable age_two con el valor: {age_two}, es mayor que la variable age_one con el valor: {age_one}")
# # Ternary operator
# im_from_navarra = True
# message = "I was born in Tudela." if im_from_navarra else "I was born in Kattegat."
# print(message)
# is_magician = True
# is_expert = False
# if is_magician and is_expert:
#     print("You are a master magician.")
# elif is_magician and not(is_expert):
#     print("At least you are getting there.")
# else:
#     print("You need magic powers.")
# for item in "Jorge Agoiz Pedraja":
#     print(item)
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for number in my_list:
#     print(number)
# Exercise: Check for duplicates in list:
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicate_values = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicate_values:
#             duplicate_values.append(value)
# print(duplicate_values)

########### Functions #############

# def say_hello(name):
#     print(f"Hello {name}")

# say_hello("Jorge")

# def first_big():
#     '''
#     This function print my name with first letter capitalized.
#     '''
#     print("jorge".capitalize())

# print(first_big.__doc__)

# Clean Code example
# def is_even(num):
#     return num % 2 == 0

# print(is_even(13))

# *args and **kwargs

# this is the default order of pass the args in this type of function
# def super_func(my_name, *args, my_num=12, **kwargs):
#     total = 0
#     print(my_name)
#     print(args)
#     print(my_num)
#     print(kwargs)
#     for items in kwargs.values():
#         total += items
#     return sum(args) + my_num + total


# print(super_func("Jorge", 1, 2, 3, 4, 5, 6, a=27, b=23))

# EXERCISE - Pass a list and give me the highest even

# my_nums = [12, 28, 27, 9, 16, 33]


# def highest_even(a_list: list):
#     a_list.sort(reverse=True)
#     for item in a_list:
#         if item % 2 == 0:
#             return item


# print(highest_even(my_nums))
