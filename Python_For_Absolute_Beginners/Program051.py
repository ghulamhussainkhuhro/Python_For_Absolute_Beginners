# Prime checker 
# Prime number are those numbers which have no unique factor.
num = int(input("Enter number you want to check whether it is prime or not : "))
i = 2
unique_factors = 0 # factors except 1 and number itself
while(i <= num):
    if(num%i == 0):
        unique_factors += 1
    i += 1
if(unique_factors == 0):
    print(num,"is a prime number!")
else:
    print(num,"is not a prime number!")

# Tip: We can also use boolean (instead of unique_factors) like a boolean named isPrime to do the same task

