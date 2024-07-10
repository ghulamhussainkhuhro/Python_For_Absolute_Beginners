# a+ mode

# open for reading and writing. THe file is created if it doeanot exists.
# The stream is positioned at the end of the file. Subsequent writes to the file will always end up at the current end of file.

f = open("demo7.txt","+a")

f.write("This is extra text written using a+ mode")