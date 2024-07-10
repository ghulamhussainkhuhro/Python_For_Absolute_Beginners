"""
Static methods: static methods in python are the functions ehich don't use self keyword
By using a decorator we can make a method static

"""

class Student:

    # Constructor
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept
    
    # Non static method---> using self as argument
    def print_info(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Dept :", self.dept)
    
    
    # Static method use decorator 
    """
    decorator allows us to wrap another function in order to extend the behaviour of the
    wrapped function, without permanently modifying it.
    
    """
    @staticmethod # decorator
    def welcome_msg():
        print("It is pleasure for us to have you in our university.")
        print("We hope you will work day and night to shine among thousands!!!")





        