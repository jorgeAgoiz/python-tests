# Person Object
# class Person:
#     '''
#         Mi primer objeto
#     '''
#     smart = True  # Static attributes

#     def __init__(self, name="unknow", age=0):
#         self.name = name  # Dinamic attributes
#         self.age = age

#     def run(self):
#         print(f"{self.name} is running!!")


# Instance of Person
# itsMe = Person("Jorge", 36)
# anotherPerson = Person()

# Some calls to obj1
# print(itsMe.name)
# itsMe.run()
# print(itsMe.smart)

# print(anotherPerson.name)
# to show all the methods of an object
# help(Person)

# Convention in Python:
# If you put underscore before methods or variables means that are privates, as you say: Hey dont touch this


# Inheritance Tests *****
class User():
    def __init__(self, fly):
        self.fly = fly

    def greet(self):
        print("Hey There!!")

    def attack(self):
        print("Im going to attack you!!!")


class IronMan(User):
    def __init__(self, city, age, fly):
        super().__init__(fly)
        self.city = city
        self.age = age

    def presentation(self):
        print(f"Im from {self.city}, and Im {self.age} years old.")

    def attack(self):
        self.greet()
        print("Iron Man shoot his laser canyon!!")


me = IronMan("Pinto", 36, True)
me.presentation()
me.attack()
print(me.fly)
print(dir(me))
