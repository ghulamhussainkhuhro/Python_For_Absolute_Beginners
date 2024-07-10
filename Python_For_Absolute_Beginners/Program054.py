# Print even numbers upto n
num = int(input("Enter number you want to print even numbers to :"))

i = 0

while(i <= num):
    if(i%2 == 0):
        print(i)
    i += 1

# Print first n even numbers 
num = int(input("Enter quantity of even numbers you want to be printed :"))

i = 0
j = 1
while(j <= num):
    print(i)
    i += 2
    j += 1

# Caution : Above two programs might seem identical 
# but there is a huge difference between them 

# upto to a number mean that is the limit to which we have to print

# but first n means no matter what the last number is, we just need that number of outputs
