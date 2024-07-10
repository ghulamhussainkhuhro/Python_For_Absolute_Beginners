# Write a recursive function to print all the elements in a list:
# Hint: use list and index as parameters 

def print_el(list, index = 0):
    if(index == len(list)):
        return 
    print(list[index])
    return print_el(list, index + 1)

list1 = [2,3,5,7,9,11]

print(print_el(list1,0))