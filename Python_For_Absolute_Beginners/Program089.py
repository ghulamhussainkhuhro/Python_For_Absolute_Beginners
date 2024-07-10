"""
from a file containing numbers separateed by comma, print count of even numbers

"""
# Method 1 to convert string into int
with open("demo10.txt", "r") as f:
    data = f.read()
    print(data)
    num = ""
    count = 0
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
# Method 2 to convert string into int
# using predefined method of python
count = 0
with open("demo10.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")

    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)
