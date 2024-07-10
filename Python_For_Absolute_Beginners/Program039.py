# Various methods/functions for python 
mydict = {
    "key"       : "Value",
    "name"      : "Ghulam Hussain",
    "cgpa"      : 3.91,
    "marks"     : [98,97,95],
    "subjects"  : ("LAAG","PS","IS","PP","ISE","OOP"),
    "Languages" : ["C++","Java","Kotlin","Python"],
    "Contact"   : "+923000000000"
}

# mydict.keys() returns all keys within a dictionary
print(mydict.keys())
print(list(mydict.keys())) # type-casted to normal list
# NOTE nested keys are not returned

#to find total number of keys
print(len(mydict.keys()))
print(len(list(mydict.keys())))

print("\n")

# mydict.values() return all values within a dictionary
print(mydict.values())
print(list(mydict.values())) # type-casted to normal list

print("\n")

# mydict.items() returns all key-value pairs as tuples

print(mydict.items())
print(list(mydict.items())) # type-casted to normal list
# We can individually excess each tuple
pairs = list(mydict.items())

print("1st tuple :",pairs[0])
print("2nd tuple :",pairs[1])
print("3rd tuple :",pairs[2])

# There are 2 methods to get the value of a key
# method 1
print(mydict["cgpa"])
# method 2
print(mydict.get("cgpa"))
# You may wonder that why are 2 different ways to do same thing reason is here:
# in case we enter a key which doesnot exists in dictionary then method 1 will throw an error
# but 2nd method instead of throwing error it will just return null value

#   method 1
# print(mydict["aaaa"]) throws error KeyError: 'aaaa'
#   method 2
# print(mydict.get("cgpa")) no error returns None

# if we want to update our dictionary we can add new key:value pairs  1 or more at a time

print(mydict)
mydict.update({"address": "Jamshoro","gender":"male"})
print(mydict)









