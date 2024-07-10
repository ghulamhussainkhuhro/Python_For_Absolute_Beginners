age  = int(input("Enter your age : "))

if(0 < age < 18):
    print("OOPs! you are not eligible to vote!")
elif(age >= 18):
    print("You are eligible to vote!")
else:
    print("Please enter a valid age number!")

# The process of giving proper spaces like in if elif or else block we are giving 4 spaces is known as indentaion