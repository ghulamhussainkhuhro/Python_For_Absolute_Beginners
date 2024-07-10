# Create a class which takes name and marks of three subjects as argumnets in a constructors
# and then a method which prints the average marks of all 3 subjects

# METHOD 2
class Student:
    # class attribute
    uni_name = "MUET Jamshoro"

    # constructor
    def __init__(self, name, marks):
        # Instance variables
        self.name = name
        self.marks = marks

    # methods or functions
 
    def print_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Average marks of ",self.name,"are ",sum/3)
    

s1 = Student("Ghulam Hussain", [78, 87, 92])
s1.print_avg()
        

