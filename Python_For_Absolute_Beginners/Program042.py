# Union & Intersection in sets

set1 = {1,2,3,4}
set2 = {1,3,5,7}

# Union: Combines both set values and returns a new set without repition of common elements same as Union in maths

print("Union:",set1.union(set2)) # this will not affect original entities of each set
union = set1.union(set2)
print("After Union Operation set1:",set1)
print("After Union Operation set2:",set2)

# Intersection: Combines common values in both sets and returns a new set of common elements same as Intersection in maths

print("Intersection:",set1.intersection(set2)) # this will not affect original entities of each set
Intersection = set1.union(set2)
print("After Intersection Operation set1:",set1)
print("After Intersection Operation set2:",set2)
