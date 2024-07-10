# Set is the collection of unordered items
# Each element in set must be unique and immutable
# boolean int float str tuple are immutable hence sa be stored in a set
# lists and dictionaries are mutable hence cannot be stored in a set

# V.N.B : Set itself is mutable but its elements are immutable

collection = {1,2,3,4,5}
print(collection)
print("Type:",type(collection))

collection1 = {1,1,2,2,"hello","hello","hello"} # in this case python will ignore all duplicate values rather than showing an error
print(collection1)
# How to create an empty set
# you might be thinking that
collection2 = {}
# This is not an set but it is empty dictionary
print(collection2)
print("Type:",type(collection2))

# So this is the correct way of creating an empty set in python
collection4 = set()
print(collection4)
print("Type:",type(collection4))
