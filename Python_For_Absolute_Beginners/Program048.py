# Print numbers from 1 to 10

i = 1
while(i <= 10):
    print(i)
    i += 1 # i = i + 1

# Print numbers from 10 to 1

i = 10
while(i >= 1):
    print(i)
    i -= 1

# Print multiplication table of a number n

n = 8
i = 1
while(i <= 10):
    print(n,"x",i,"=",i*n)
    i+=1

# Print first n squares

i = 1
while(i <= 10):
    print("Square of",i,"is :",i*i)
    i+=1

list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Traverse through all elements of list using while loops
i = 0
while(i < len(list1)):
    print("Element at index",i,"is :",list1[i])
    i += 1

