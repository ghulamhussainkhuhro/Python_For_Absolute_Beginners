# del keyword in puthon
# it is used to delete object properties or object itself
"""
let say s1 is an instance of class Student
del s1.name will delete the name attribute in s1 object
del s1 will delete entire s1 object

"""

class Student:

    def __init__(self,name, grade):
        self.name = name
        self.grade = grade
    
    def show_data(self):
        print(self.name, "studies in", self.grade)

s1 = Student("Ghulam Hussain", "2nd year")
# Before deleting name variable we can access it without error
print("Name of student is ", s1.name)

# After deleting name variable we cannot access it, it will lead to an error
del s1.name
# print("Name of student is ", s1.name) # AttributeError: 'Student' object has no attribute 'name'

del s1 
# s1.show_data() #NameError: name 's1' is not defined
        
