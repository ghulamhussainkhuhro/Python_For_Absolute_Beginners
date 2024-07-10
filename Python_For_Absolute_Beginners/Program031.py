# Different pre-defined_ methods used in lists

# list_name.append() adds entity at the last of a list

list = [2, 1, 4]
list.append(5)
print(list.append(3)) # Gives None value
print(list)

# sort() sorts in ascending order
print(list.sort()) # This will always return None but you can access sorted list by just calling it
print("Ascending order : ",list)

# sort( reverse = True) sorts in descending order
print(list.sort(reverse=True)) # This will always return None but you can access sorted list by just calling it
print("Descending order : ",list)

# Sorting  is applicable for Strings in a list as well

fruits = ["Mango", "Banana", "Watermellon"]
print("Before sorting : ", fruits)

fruits.sort()
print("In Ascending order sorting : ", fruits)

fruits.sort(reverse= True)
print("Sorting in decreaing order : ", fruits)

list = ["d", "b", "a", "c", "g", "f", ]
print("Before reversing,",list)
list.reverse()
print("After reversing,",list)

#list.insert(index,el) # Insert elements at index

print(list)
list.insert(1,99)
print(list)


# list.remove(1) :REmoves the firsst occurence of data
list1 = [2,3,8,4]
list1.remove(8)
print(list1)

# list1.pop(index)  : Removes elements at index

list1.pop(2)
print(list1)
