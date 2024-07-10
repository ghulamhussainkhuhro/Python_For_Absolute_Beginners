# Reason for single double and triple strings qoutaions in puthon

print("He is 'Boy'")
print('He is "Boy"')
print(''''He' is "Boy"''')

# Joining two or more strings together is known as concatenation
str1 = "Ghulam"
str2 = "Hussain"

str3 = str1+" "+str2

print("My name is",str3)

# Length of string : Number of charachters including whitespaces

print("Length of str1 is : ",len(str1))
print("Length of str2 is : ",len(str2))
print("Length of str3 is : ",len(str3))

# Indexing
print("Character at index 0 of str3 is str3[0]",str3[0])
print("Character at index 1 of str3 is str3[0]",str3[1])
print("Character at index 7 of str3 is str3[0]",str3[7])
print("Character at index 12 of str3 is str3[0]",str3[12])
print("Character at index 13 of str3 is str3[0]",str3[13])
# We cannot assign any value of our choice at any index of string because simply they are immutable

# Slicing in strings
# syntax : str_name[starting_index : ending_index]
# Note: Ending_index will not be included!

name = "Ghulam Hussain Khuhro"
first_name = name[0:6] # or name[:6]
mid_name = name[7:15]
last_name = name[15:21]# or name[15:] or name[15:len(name)]
print("Full name :",name)
print("First name : ", first_name)
print("Mid name :",mid_name)
print("Last name : ",last_name)

#Slicing in Negative indexing 
l_name = name[-7:]
m_name = name[-15:-7]
f_name = name [-22:-15]

print("Full name :",name)
print("First name : ", f_name)
print("Mid name :",m_name)
print("Last name : ",l_name)


# Python also supports negative indexing like last index will be -1,-2,-3,-4,... and so on!
