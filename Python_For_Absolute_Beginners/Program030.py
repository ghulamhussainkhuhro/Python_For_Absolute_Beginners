# Silicing in lists
# It is similar to string slicing
# syntax : list_name[starting_index : ending_index]
# NOTE : Ending index is not included!

marks = [85, 94, 76, 63, 48]

print("Traditional indexing : ")
print(marks[:3])
print(marks[1:3])
print(marks[3:3])
print(marks[2:])
print()

# THe concept of negative indexing is same for the list as well!


print("Negative indexing : ")
print(marks[-3:-1])
print(marks[-2:])
print(marks[:-1])
print(marks[-2:-1])
