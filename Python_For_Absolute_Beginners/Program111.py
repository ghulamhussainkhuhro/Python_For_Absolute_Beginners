# Property decorator: 
# We use @property decorator on any method in the class to use the method as the property 

# Below given method is also correct but we may use even a better way using property decorator see Program112.py
class Student:
    def __init__(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem
    
    def calc_perc(self):
        self.percentage = str((self.math + self.phy + self.chem)/3) + "%"
        return self.percentage
    

s1 = Student(75,80,97)
print("Physics marks :",s1.phy)
print("Percentage : ",s1.calc_perc())
s1.phy = 56
s1.calc_perc()
print("Physics marks :",s1.phy)
print("Percentage : ",s1.calc_perc())



