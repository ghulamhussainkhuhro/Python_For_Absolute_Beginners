# with Syntax

# Using with condition to read a file
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
    # file will be automiatically closed in this syntax we don't need to do this manually

# Using with condition to write a file

with open("demo.txt", "w") as f:
    f.write("This is new text in the file\n")
    f.write("I have uploaded it using with syntax")

# Using with condition to read write a file

with open("demo.txt", "a+") as f:
    f.write("\nHello brotha!!!")
    print(data)


