# Write a function which takes a number as an argument and checks
# whether the number is prime or not

def check_prime(num):
    if(num == 1):
        print("1 is neither prime nor composite")
    elif(num <= 0):
        print("Please enter a valid natural number.")
    elif(num >= 2):
        for i in range(2,int(num**0.5)+1):
            if(num % i == 0):
                print(num,"is not a prime number")
                break
        else:
            print(num,"is prime")
                

check_prime(-1)
check_prime(0)
check_prime(1)
check_prime(2)
check_prime(4)
check_prime(99991)