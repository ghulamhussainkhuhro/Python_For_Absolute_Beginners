# Print numbers from 0 to 10 except 5
i = 0
while(i <= 10):
    if(i == 3):
        print("Guess what?, I escaped a number!")
        i += 1
        continue
    print(i)
    i += 1