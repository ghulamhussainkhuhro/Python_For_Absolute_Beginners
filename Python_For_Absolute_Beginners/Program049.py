# Searching an element in a tuple:

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print("Here is tuple : ",tup)
tosearch = int(input("Enter number you want to search : "))  

# break : is used to terminate the loop when encountered 
# continue : terminates execution in the current iteration  and continues execution of loop with the next iteration

# Method 1 ---> using break Recommended in this situation 
i = 0
while(i < len(tup)):
    print("Iteration ",i+1)
    if(tup[i] == tosearch):
        print("Number found at index :",i)
        break
    i += 1

# Method 2 ---> using continue Not recommended in htis situation
i = -1
while(i < len(tup)):
    print("Iteration ",i+1)
    i += 1
    if(tup[i] != tosearch):
        continue
    else:
        print("Number found at index :",i)
        break
    