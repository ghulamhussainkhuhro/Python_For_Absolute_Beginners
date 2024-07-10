# Write a function to print the factorial of a number

def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

num = int(input("Enter a number you want to finf factorial of : "))

print("Factorial of",num,"is :",calc_fact(num))