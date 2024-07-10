# Search for a number x in this tuple using loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

sq_nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,81]

print("Here is the list :",sq_nums)

num = int(input("Enter the number you want to search for : "))

idx = 0
for el in sq_nums:
    if(el == num):
        print("Element found at index",idx)
    idx += 1
else:
    print("Element not found")
