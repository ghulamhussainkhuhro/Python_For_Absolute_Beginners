def checker(num):
    print("Even") if(num%2 == 0) else print("Odd")

char = "y"

while(char == "y"):
    num = int(input("Enter a number to check : "))
    checker(num)
    print("Do you want to comtinue ?(y/n)", end=" ")
    char = input()
    if(char == "y"):
       continue
    else:
        break
    