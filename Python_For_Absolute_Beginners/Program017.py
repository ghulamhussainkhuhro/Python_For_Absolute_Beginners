# Type conversion and type casting

#Type conversion is automatically done by the python interpreter
#For example 
a = 2 #int
b = 3.59 # float

sum1 = a + b # here a is automatically converted as float and results as a floating number

print("Sum is : ",sum1)

#type casting refers to the manual conversion from one type to another
#for example 
c = "2"
d = 3.591
# print(c+d) TypeError: can only concatenate str (not "float") to s
sum2 = float(c)+d
print(sum2)

val1 = True
val2 = True

print("Sum of val1 and val2 is : ", int(val1)+int(val2))

num = 3.14
print(type(num))
num = str(num)
print(type(num))

