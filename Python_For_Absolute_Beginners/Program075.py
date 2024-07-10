# WAP to calculate the sum of first n natural numbers

def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) + n

num = int(input("Enter a number : "))
print("Sum of first",num,"natural numbers is :",cal_sum(num))