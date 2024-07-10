# WAP to find the factorial of first n numbers
# Method 1 ---> 
num = int(input("Enter number to print its factorial: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial of",num,"is :",fact)

# Method 2 ---> 
num = int(input("Enter number to print its factorial: "))
fact = 1
i = 1
while(i <= num):
    fact *= i
    i += 1
print("Factorial of",num,"is :",fact)


