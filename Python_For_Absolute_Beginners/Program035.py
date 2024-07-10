# WAP to chack if a list contains a palindrome of elements 
# Hint : use copy() method

list1 = [1,2,3,2,1]
list2 = ["Ball", "Bat", "Pitch", "Bat", "Ball"]
list3 = [1, 2, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()
copy_list2 = list2.copy()
copy_list2.reverse()
copy_list3 = list3.copy()
copy_list3.reverse()


print(list1,"is palindreome") if (copy_list1 == list1) else print(list1,"is not palindrome")
print(list2,"is palindreome") if (copy_list2 == list2) else print(list2,"is not palindrome")
print(list3,"is palindreome") if (copy_list3 == list3) else print(list3,"is not palindrome")

