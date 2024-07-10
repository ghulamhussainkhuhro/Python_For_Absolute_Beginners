# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# start with an empty dictionary and add one by one . Use subject name as key and marks as values.

result = {

}
# We can add all subjects & marks at once but question say to add one by one
result.update({"OOP" : 137})
result.update({"LAAG" : 92})
result.update({"ISE" : 86})
result.update({"PP" : 92})
result.update({"IS" : 45})
result.update({"PS" : 46})

print(result)
print("In list form:",list(result))
print("Type :",type(result))

# Taking marks from user as input :


marks = {}

x = int(input("Enter marks for OOP: "))
marks.update({"OOP" : x})

x = int(input("Enter marks for LAAG: "))
marks.update({"LAAG" : x})

x = int(input("Enter marks for ISE: "))
marks.update({"ISE" : x})

x = int(input("Enter marks for PP: "))
marks.update({"PP" : x})

x = int(input("Enter marks for IS: "))
marks.update({"IS" : x})

x = int(input("Enter marks for PS: "))
marks.update({"PS" : x})

print(marks)
print("In list form:",list(marks))
print("Type :",type(marks))


