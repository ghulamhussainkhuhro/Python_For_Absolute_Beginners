# Write a function to concert PKR to USD

def pkr_to_usd(pkr, current_rate = 281.13):
    return pkr/current_rate

amount = float(input("Enter amount in PKR : "))

print(amount,"ruppees are equal to",pkr_to_usd(amount),"dollars")