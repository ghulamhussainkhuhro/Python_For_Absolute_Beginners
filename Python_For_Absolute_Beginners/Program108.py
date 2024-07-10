# class method : A class method is bound to the class and receives the class as an i,plicit first argument

# non static methods cannot access or modify class state and generally for utility

class Person:
    name = "anonymous"
    # what you think that how can we change this class attribute

    def change_name(self, name):
        self.name = name
    
        
    # There are several ways to change the class attribute's value in indirect way
    # instead of self.name = name we could have written Person.name = name

    # Method 1 --->
    def change_name1(self, name):
        Person.name = name

    # Method 2 --->

    def change_name2(self, name):
        self.__class__.name = name

    # Method 3 --->

    # We can use class method decorators

    @classmethod
    def change_name3(cls, name):
        cls.name = name

    
p1 = Person()
p1.change_name("Ghulam Hussain")
print(p1.name)# output : Ghulam Hussain
# name is changed to Ghulam Hussain but only for newly created instance varaible,
# original name (i.e. class variable) is still same
print(Person.name)

    
