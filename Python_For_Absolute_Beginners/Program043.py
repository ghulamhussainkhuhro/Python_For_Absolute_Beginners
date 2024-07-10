# Store the following word meanings in python dictionary:
# table : "a piece of furniture", "list of facts and figures"
# cat : a small animal
# Method 1 --->
mydict = {
    "cat" : "a small animal",
    "table" : {
        "meaning1" : "a piece of furniture",
        "meaning2" : "list of facts and figures"
    }
}
print("Method 1: Dictiobary :",mydict)
# We can also store different maeanings in by using lists or tuples too instead of nested dictiionary      

# Method 2 --->
mydict1 = {
    "cat"   : "a small animal",
    "table" : ["a piece of furniture","list of facts and figures"]
    }
print("Method 2: Dictiobary :",mydict1)
# Method 3 --->
mydict2 = {
    "cat" : "a small animal",
    "table" : ("a piece of furniture","list of facts and figures")
}
print("Method 3: Dictiobary :",mydict2)

# Method 4 --->
mydict3 = {
    "cat" : "a small animal",
    "table" : {"a piece of furniture","list of facts and figures"}
}
print("Method 4: Dictiobary :",mydict3)