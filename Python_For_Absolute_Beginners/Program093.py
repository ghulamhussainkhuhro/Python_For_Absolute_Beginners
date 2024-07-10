# Contructor(init function) overloading in python
# We can have more than 1 init() with different arguments

class Student:

    # Default Constructor
    def __init__(self):
        print("Creating an instance of student using default constructor!")

    # Parameterized Constructor
    def __init__(self, name):
        print("Creating an instance of student using parameterized contructor")
        self.name = name
    
s2 = Student()
s1 = Student("Ghulam Hussain")
print("Name :", s1.name)
s3 = Student("Shafique")
print("Name :", s3.name)




