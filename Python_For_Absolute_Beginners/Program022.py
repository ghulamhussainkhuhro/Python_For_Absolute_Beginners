# Different Functions for strings

#endswith() returns true if string ends with that sub string
str = "ghulam Hussain"
print(str.endswith("oin"))
print(str.endswith("ain"))

#capitalize(): capitalize first charachter
print(str.capitalize()) # does not affect the original string
print(str) # original string
str = str.capitalize() # assiging modified value to a new string for permanent change
print(str)

# replace(old,new)
print(str.replace("a","@"))
print(str.replace("hussain","Mustafa"))

#find(word): returns 1st index of 1st occurrence
print(str.find("m"))

#count("substring"): counts the occurrence of a substring
str1 = "the pen which he gave me last week is not writing on the page correctly."
print(str1.count("the"))
print(str1.count(str1))


