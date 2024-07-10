def max(val1, val2, val3):
    if(val1 > val2 and val1 > val3):
        print(val1,"is greatest.")
    elif (val2 > val1 and val2 > val3):
        print(val2,"is greatest.")
    else:
        print(val3,"is greatest")

print(max(5,2,6))
