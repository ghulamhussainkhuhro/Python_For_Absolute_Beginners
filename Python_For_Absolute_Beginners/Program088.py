""""
Task 1: Create a new file demo9.txt usinf python and add the following data in it

Hi everyone
We are learning file I/O
Using Java.
I like programing in Java.

"""

with open("demo9.txt", "w+") as f: # This will create the file named demo9.txt and will add text in tit
    f.write("Hi everyone\n")
    f.write("We are learning file I/O\n")
    f.write("Using Java.\n")
    f.write("I like programing in Java.\n")
    
with open("demo9.txt","r") as f:
    d = f.read()
    print(d)
    

""""
Task 2: Write a function that replaces all the occurences of "java with python" in above file

"""
# To do this first we need to know what is in our file i.e. we have to read it

with open("demo9.txt", "r") as f:
    data = f.read()

# now we need to replace word Java by python
new_data = data.replace("Java", "Python")
print(new_data)

# now we need to save i.e overrite these changes to our original file

with open("demo9.txt", "w") as f:
    f.write(new_data)



""""
Task 3: search if the word learning exists in the file or not

"""
word = "learing"
with open("demo9.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1): # we can also write it as if(word in data)
        print("Yes learning word is in the file.")

""""
Task 4: Write a function to find in which line of the file does the word learning  occurs the first 
print -1 if the word not found!!!

"""

def check_for_line():
    word = "programing"
    data = True
    line_no = 1
    with open("demo9.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1 # if the word is not in the file

print(check_for_line())




