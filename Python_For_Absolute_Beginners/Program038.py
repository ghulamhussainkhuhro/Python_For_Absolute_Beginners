# Nested Dictionaries
student = {
    "name" : "Ghulam Hussain",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student)

# Accessing nested values in keys
print("Marks in physics :",student["subjects"]["phy"])
print("Marks in chemistry :",student["subjects"]["chem"])
print("Marks in mathematics :",student["subjects"]["math"])