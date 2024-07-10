# Dictionary in python
# Dictionaries are used to store data values in key:value pairs
# They are unordered(Because there is no any indexing like in strings,lists or tuples), mutable(changeable) & don't allow duplicate keys

dict = {
    "key"       : "Value",
    "name"      : "Ghulam Hussain",
    "cgpa"      : 3.91,
    "marks"     : [98,97,95],
    "subjects"  : ("LAAG","PS","IS","PP","ISE","OOP"),
    "Languages" : ["C++","Java","Kotlin","Python"],
    "Contact"   : "+923000000000"
}

#NOTE it is not necessary that keys should be only strings we can maake keys int and float as well

# Dictionary data
print(dict)
# accessing values through keys
print(dict["name"])
# Updating values through keys
dict["name"] = "GHK"
dict["marks"] = (1,2,3,4,5)
print(dict)
# Printing the type of dictionary
print(type(dict))

# print(dict["CGPA"]) KeyError: 'CGPA' This error indicates that there is no key named as CGPA in dict
