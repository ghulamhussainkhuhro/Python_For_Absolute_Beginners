# Function : Block of statements that performs a specific task

# Function definition
def sum(a, b): # a and b are known as parameters
    sum = a + b# body of function
    return sum # return statement 

def diff(a, b):
    diff = a - b
    return diff

def product(a, b):
    product = a * b
    return product

def qoutient(a, b):
    qoutient = a / b
    return qoutient

def modulo(a, b):
    modulo = a % b
    return modulo

def power_to_base(b, p):
    result = b ** p
    return result

#**************** Calculator using functions*******************

num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))

# sum(num1,num2) # Function call, num1 and num2 are called arguments

print("Sum of ",num1,"and",num2,"is : ",sum(num1,num2))
print("Difference of ",num1,"and",num2,"is : ",diff(num1,num2))
print("product of ",num1,"and",num2,"is : ",product(num1,num2))
print("qoutient of ",num1,"and",num2,"is : ",qoutient(num1,num2))
print("Remainder of ",num1,"divided by",num2,"is : ",modulo(num1,num2))
print(num1,"raised to powewr",num2,"is : ",power_to_base(num1,num2))
