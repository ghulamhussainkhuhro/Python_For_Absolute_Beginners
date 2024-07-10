# slicing in tuples

tup = (1, 2, 3, 4, 5)
print(tup[1:3])
print(tup[:3])
print(tup[0:])

# Finding index of an element in tuple

# Finding index of 2 in the given tuple 
print(tup.index(2))
# print(tup.index(6))ValueError: tuple.index(x): x not in tuple

tup1 = (4, 5, 6, 1, 5, 3, 4, 5, 8, 9, 11, 5)
# tuple.count(num) is used to find no of times an element exists in a tuple
print("Occurence of 5 in tup1 is",tup1.count(5),"times.")



