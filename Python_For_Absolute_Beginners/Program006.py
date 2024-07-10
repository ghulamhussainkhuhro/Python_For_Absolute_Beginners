# Numeric values can operate with all arithmetic operators
a = 2
b = 5
c = a*10


print(a+b*c)
print(a/b)
print(type(a/b))

# Arithmetic expressions with integers and float results into float

num1 = 8
num2 = 2.0

sum = num1+num2
diff = num1-num2
product = num1*num2
qoutient = num1/num2

print("Sum of ",num1 , "and", num2, "is : ",sum)
print("Difference of ",num1 , "and", num2, "is : ",diff)
print("Product of ",num1 , "and", num2, "is : ",product)
print("Qoutient of ",num1 , "and", num2, "is : ",qoutient)

print()
print("Types of result")

print("Sum of ",type(num1) , "and", type(num2), "is : ",type(sum))
print("Difference of ",type(num1) , "and", type(num2), "is : ",type(diff))
print("Product of ",type(num1) , "and", type(num2), "is : ",type(product))
print("Qoutient of ",type(num1) , "and", type(num2), "is : ",type(qoutient))


