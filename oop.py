# Person Object
class Person:
    '''
        Mi primer objeto
    '''
    smart = True  # Static attributes

    def __init__(self, name="unknow", age=0):
        self.name = name  # Dinamic attributes
        self.age = age

    def run(self):
        print(f"{self.name} is running!!")


# Instance of Person
itsMe = Person("Jorge", 36)
anotherPerson = Person()

# Some calls to obj1
print(itsMe.name)
itsMe.run()
print(itsMe.smart)

print(anotherPerson.name)
# to show all the methods of an object
# help(Person)
