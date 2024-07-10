# Methods in classes

class Student:
    # class attribute
    uni_name = "MUET Jamshoro"

    # constructor
    def __init__(self, name, age, dept):
        # Instance variables
        self.name = name
        self.age = age
        self.dept = dept

    # methods or functions
    def pay_fee(self):
        print(self.name,"paid semester fees")
    
    def study(self, duration, place):
        print(self.name,"study for ",duration, "hours at",place)

    def get_age(self):
        return self.age
    
s1 = Student("Ghulam Hussain",19,"BE SWE")
print("Name :",s1.name)
print("Age :",s1.name)
print("Dept :",s1.name)
print("Uni :",Student.uni_name)
s1.pay_fee()
s1.study(8,"Central Library")
print("Age of",s1.name,"is",s1.get_age())