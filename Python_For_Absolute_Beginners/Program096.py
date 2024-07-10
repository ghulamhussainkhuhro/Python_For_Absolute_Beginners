# Create a class which takes name and marks of three subjects as argumnets in a constructors
# and then a method which prints the average marks of all 3 subjects

# METHOD 1
class Student:
    # class attribute
    uni_name = "MUET Jamshoro"

    # constructor
    def __init__(self, name, math, chem, phy):
        # Instance variables
        self.name = name
        self.math = math
        self.chem = chem
        self.phy = phy

    # methods or functions
 
    def print_avg(self):
        marks = (self.math + self.chem + self.phy)/3
        print("Average marks of ",self.name,"are ",marks)
    

s1 = Student("Ghulam Hussain", 78, 87, 92)
s1.print_avg()
        

