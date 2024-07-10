# WAP, Figure out a way to store 9 & 9.0 as separate values in the set.
# Hint: You can take help of builtin data types

# method 1 --->
set1 = {
    9, "9.0"
}
print("Method 1 ---> : ",set1)

# method 2 --->
set2 = {
    9.0, "9"
}
print("Method 2 ---> : ",set2)

# method 3 --->
set3 = {
    ("float" , 9.0),
    ("int" , 9)
}
print("Method 3 ---> : ",set3)
print("Method 3 ---> : ",list(set3))


