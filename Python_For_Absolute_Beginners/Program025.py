# eligiblity  for president election:
# Nested conditions
age = int(input("Enter your age : "))
nationality = input("What is you nationality :")

if(age >= 35):
    if(nationality == "Pakistani"):
        print("You are eligible to be a president!")
        print("Fill out given forms...")
    else:
        print("You are not eligible for being president!")
        print("Reason: You are not pakistani")
else:
    if(nationality == "Pakistani"):
        print("You are not eligible to be a president!")
        print("Reason: Because your age is less than 35 years!")
    else:
        print("You are not eligible to be a president!")
        print("Reason: Neither you are Pakistani nor your age is greater than or equal to 35!")
    