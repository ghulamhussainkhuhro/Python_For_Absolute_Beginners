# Write in a file
"""
    There are two modes of writing in a file "w" and "a" mode 
    in w mode existing data is reased and new data is added
    in a mode new data is added at the end of existing data

"""
 
# Opening file in write mode(Overwriting)

f = open("demo4.txt","w")
# now anything we will write in this file will totly raplace the existing file
f.write("New data is written in demo4.txt\n") # we have to explicitly add the new line
f.write("Hello World!\n")

f.close()

#Openning file in append mode(adding at the end)

f = open("demo4.txt", "a")
# now anything we will write in this file will be added at the end of existing text
f.write("This is appended text in the demo4.txt\n")
f.write("Hello Wolrd\n")

# Note: Sometimes the file we want to open in w or a mode doesnot exist 
# in that case a new file is automatically created for us
