# Tuples
# A built-in data type that lets us create immutable sequence of values

tup = (87, 64, 33, 95, 76)
print(tup)
print(tup[0],tup[1],tup[4])
print("Type : ",type(tup))

# tup[0] = 100 TypeError: 'tuple' object does not support item assignment. This is not allowed in python!
# In list we can do this but in strings and tuples assignment is not allowed

# Empty tuple

tup1 = ()
print("Empty tuple :",tup1)
print("Type :",type(tup1))

# Single valued tuple
tup2 = (2,) # comma is must if you will not give comma python will treat that as an int value
tup3 = (3)  # Python will treat it as an int value

print("Single valued (with comma) :",tup2)
print("Type :",type(tup2))

print("Single valued (without comma) :",tup3)
print("Type :",type(tup3))

tup4 = ("Hello") # Type will be str
print(type(tup4))
tup5 = ("Hello",)# Type will be tuple
print(type(tup5))



