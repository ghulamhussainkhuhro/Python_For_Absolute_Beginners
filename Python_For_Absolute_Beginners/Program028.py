# List in python!
# A built-in data type that stores set of values
# It can store elements of different types
# marks1 = 10
# marks2 = 19.5
# marks3 = 98.7
# marks4 = 87.3
# marks5 = 55.3
# marks6 = 88.2
# marks7 = 71.19
# marks8 = 82.5
# marks9 = 76.42

# Instead of making so many different variables, We can use lists
marks = [10, 19.5, 98.7, 87.3, 55.3, 88.2, 71.19, 82.5, 76.42]
print("Elements of list : ",marks)
print("Type of list : ",type(marks))

# We can access elemnt at any index in alist
print("Element at index zero is :",marks[0])
print("Element at index 7 is :",marks[7])
print(marks[len(marks)-1]) # element at last index!

# We can store different data type entities in a single list

student_info = ["Ghulam Hussain", 19, "23SW050", +923000000000, 69350]
print("Student's data is :",student_info)
