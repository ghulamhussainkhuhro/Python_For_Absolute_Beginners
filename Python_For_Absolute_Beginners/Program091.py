"""
__init__() [init function] in Python
All classes have a function called __init__() which is always executed when the object is being executed
whether you you write or not init function is always executed
we can also called the init function as Constructor
__init__() always takes an argumnet known as self
The self parameter is a reference to the current instance of the class(i.e. object), 
and is used to acess variables that belong to the class
self is always the first parameter

"""

class Student:
    def __init__(self):
        print(self) # this will print the location of the object
        print("New Student added to the database...")
    name = "Ghulam Hussain"
    grade = "2nd Year BE Student"
    age = 19

s1 = Student()
print(s1)
s2 = Student()
print(s2)
s3 = Student()
print(s3)


