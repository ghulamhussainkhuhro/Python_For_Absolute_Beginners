# w+ mode

f = open("demo6.txt","w+" )

f.write("Old text will be replsced by this line.")

print(f.read())

f.close()