# For lopp in python 
# For loops are genrally used for sequential traversal. For traversing
# lists , strings, tuples etc.

# Treversing through a list using for loop
nums = [1, 2, 3, 4, 5]
veggies = ["potato", "Brinjal", "ladyfinger"]

for val in nums:
    print(val)
for val in veggies:
    print(val)

# Treversing through a String using for loop
str = "Ghulam Hussain"
print("Case 1:\n")

for char in str:
    print(char)
else:
    print("End of loop")

print("Case 1:\n")
for char in str:
    if(char == 's'):
        print("s found")
        print("else block will not execute")
        break
    print(char)
else:
    print("End of loop")

# We can use an optional else along with  for loop to be executed when the loop completes not break

