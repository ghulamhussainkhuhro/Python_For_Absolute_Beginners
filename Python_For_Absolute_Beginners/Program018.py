# input() is used to accept the values (using keyboard from user)

#input() result for this is always a str

val = input("Enter anything you want : ")
print(type(val))
# No matter you enter floating number integer boolean or string it will always give an string 

# to get the desired input i.e. int or float you must type cast it

val = int(input("Enter your age : "))
print(type(val))

val = float(input("Enter your salary: "))
print(type(val))



