# Write a function to print the elements of a list in a single line(list is the parameter)

def print_list(list):
    print(list)
    for i in list:
        print(i,end=" ")

list1 =[2,4,7,8,13]

print_list(list1)
