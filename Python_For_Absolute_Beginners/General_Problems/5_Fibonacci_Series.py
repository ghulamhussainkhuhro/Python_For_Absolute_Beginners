def print_fibo(num):
    a = 0
    b = 1
    temp = 0
    print(a,b,sep="  ",end="  ")
    for i in range(3,num+1):
        temp = a
        a = b
        b = temp + a
        print(b,end="  ")

print_fibo(10)




    