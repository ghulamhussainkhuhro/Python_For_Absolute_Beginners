# WAP to get the sum of n numbers

# Method 1 
n = int(input("Enter number to which you want to print sum : "))
sum = 0

for i in range(1,n+1,1):
    sum += i
print("Sum of first",n,"natural numbers is :",sum)

# Method 2
n = int(input("Enter number to which you want to print sum : "))
sum = 0
i = 1
while(i <= n):
    sum += i
    i += 1
print("Sum of first",n,"natural numbers is :",sum)


