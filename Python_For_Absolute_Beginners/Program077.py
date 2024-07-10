# File I/O in python
# Open read and closing a file
# Open
file = open("demo.txt","r")
#read
data = file.read()
print(data)
print(type(data))

#close
file.close()

# Different modes
# r --> open for reading(default) 
# w --> open for writing, truncaating the file first(i.e deleting all the existing data first)
# x --> create a new file and open it for writing 
# a --> open for writing, appending at the end of the file if exists
# b --> binary mode
# t --> text mode (default)
# + --> open a disk file for updating (reading and writing)