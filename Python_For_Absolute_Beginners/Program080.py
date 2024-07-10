f = open("demo3.txt", "r")

# Read
data = f.read()
print("Reading the file: ")
print(data)

# Once you read all the data you cannot not read it again untill and  unless you closse and reopen it

data = f.read()
print("Reading the file agian: ")
print(data)
# You may see in output that it is empty

# to read it gain lets close and reopen it

f.close()

f = open("demo3.txt", "r")
# Read
data = f.read()
print("Reading the file: ")
print(data)
