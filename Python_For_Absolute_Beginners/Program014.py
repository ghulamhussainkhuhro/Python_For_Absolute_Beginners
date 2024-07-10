# Clever if / ternary operator
# syntax of clever if is # <var> = (false_value, true_value) [condition]

age = int(input("Enter your age : "))
vote = ("no","yes") [age>=18]
print("Can you vote ?", vote)

salary = float(input("Enter your salary : "))
tax = salary*(0.1,0.2) [salary >= 50000]
print("Tax on your income",salary,"is",tax)

