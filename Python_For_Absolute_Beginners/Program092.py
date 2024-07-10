# Passing parameters in _init__()

class Student:
    def __init__(self,name, age, grade) -> None:
        print("Creating an instance of student whose name is ",name)
        self.name = name
        self.age = age
        self.grade = grade

s1 = Student("Ghulam Hussain", 19, "2nd year")
print("Name :", s1.name)
print("Age :", s1.age)
print("Grade :", s1.grade)

s2 = Student("Sarmad", 18.5, "2nd year")
print("Name :", s2.name)
print("Age :", s2.age)
print("Grade :", s2.grade)

s3 = Student("Shafique", 18, "2nd year")
print("Name :", s3.name)
print("Age :", s3.age)
print("Grade :", s3.grade)



