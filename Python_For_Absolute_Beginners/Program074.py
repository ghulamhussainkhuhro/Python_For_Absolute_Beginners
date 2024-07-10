# Factorial Through recursion:
def calc_fact(n):
    if(n == 0 or n == 1):
        return 1
    print("n is ",n)
    return n * calc_fact(n - 1 )
    

num = int(input("Enter a number : "))
print("Factorial of",num,"is :",calc_fact(num))

# Short method
def fact(n):
    if(n == 0 or n == 1):
        return 1
    return n * fact(n-1)
print("factorial of 5 is :",fact(5))