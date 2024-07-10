# class attributes and object attributes
"""

class attributes: Those attributes which can be same for all the instances of a class
                  Like name of college of a group of students

object attributes: Those attributes which are unique for all different instances of a class
                   Like name and roll no: of every student differ from one another

                   Whenever there is same name of class and obj attribute 
                   then precedence is always given to obj attribute

"""

class Student:
    uni_name = "MUET Jamshoro"
    nationality = "Pakistani"

    def __init__(self, name, age, dept) -> None:
        self.name = name
        self.age = age
        self.dept = dept

s1 = Student("Ghulam Hussain",19,"Dept: of Software Engineering")
print("Name :",s1.name)
print("Age :",s1.age)
print("Dept :",s1.dept)
print("Uni_name :",Student.uni_name) # Accessing diectly using class name
print("Nationality :",Student.nationality)

s2 = Student("Fardeen", 20, "Dept: of Mechanical Engineering")
print("Name :",s2.name)
print("Age :",s2.age)
print("Dept :",s2.dept)
print("Uni_name :",Student.uni_name) # Accessing diectly using class name
print("Nationality :",Student.nationality)

        
