# Write a program to create and print the list of squares 
# where numbers are between 1 and 30

def print_squares():
    list1 = []
    for i in range(1,31):
        list1.append(i**2)
    return list1

print(print_squares())