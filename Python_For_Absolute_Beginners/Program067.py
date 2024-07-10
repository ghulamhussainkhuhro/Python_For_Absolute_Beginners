# Default argumnets in functions : It helps us when we donot pass an argument 
# a default value is set hence no error is produced

def calc_prod(a = 1, b = 1):
    return a * b

print("0 Arguments Product is :", calc_prod()) 
print("1 Argument Product is :", calc_prod(3))
print("2 Arguments Product is :", calc_prod(4,7))

# We can set single, few or all arguments as default it is upto to our matter of choice!
