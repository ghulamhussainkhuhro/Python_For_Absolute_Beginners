# Property decorator: 
# We use @property decorator on any method in the class to use the method as the property 

# This is the best way to solve problem we faced in Program110.py
class Student:
    def __init__(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem

    @property
    def calc_perc(self):
        return str((self.math + self.phy + self.chem)/3) + "%"
        
    

s1 = Student(75,80,97)
print("Physics marks :",s1.phy)
print("Percentage : ",s1.calc_perc)
s1.phy = 56
# Now when we will update marks percentage will be also updated
print("Physics marks :",s1.phy)
print("Percentage : ",s1.calc_perc)
# See here calc_perc is now not called as a method but as an attribute



