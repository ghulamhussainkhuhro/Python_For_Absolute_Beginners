# Recursion : When a function calls itself repeatedly 

def show(n):
    if(n == 0): # Base case: i.e. stopping case for recursion
        return
    print("Show :",n)
    show(n-1)
    print("Ended ",n)

show(3)