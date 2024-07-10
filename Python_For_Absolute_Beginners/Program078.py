# Once you read a file partially or fully you cannot read ot again !
# you can imagine it as if there is a cursor which continues moving forward as long as you are reading 
# once you read the whole file , it cannot move back
# if there are 20 numbers in a row and you are reading 10 charcters two time then at first there will be
# first 10 and then at 2nd it will read from 11th character

# read only 30 charachters 
f = open("demo1.txt","r")

print("Reading 5 characters :")
data1 = f.read(5)
print(data1)

print("Reading 5 characters :")
data1 = f.read(5)
print(data1)

print("Reading 5 characters :")
data1 = f.read(5)
print(data1)

print("Reading 5 characters :")
data1 = f.read(5)
print(data1)

print("Reading 5 characters :")
data1 = f.read(5)
print(data1)

print("Reading 5 characters :")
data1 = f.read(5)
print(data1)


