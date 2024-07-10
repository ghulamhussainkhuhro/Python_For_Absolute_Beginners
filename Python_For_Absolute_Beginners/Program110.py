# Property decorator: 
# We use @property decorator on any method in the class to use the method as the property 

class Student:
    def __init__(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem
        self.percentage = str((self.math + self.phy + self.chem)/3) + "%"

s1 = Student(75,80,97)
print("Physics marks :",s1.phy)
print("Percentage : ",s1.percentage)
s1.phy = 56
print("Physics marks :",s1.phy)
print("Percentage : ",s1.percentage)

# Now if we will update any subject's marks they will be updated but the percentage will reamain same 
# so we need separate method which must update the percentage 

# See Program111.py to see solution to this problem

