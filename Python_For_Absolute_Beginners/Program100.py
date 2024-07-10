# Create an account class with two attributes - balance and account no
# create methods for debit credit and printing the balance

class Account:
    def __init__(self, account_no, balance = 11000):
        self.account_no = account_no
        self.balance = balance
        print("Account created and added to database...")
    
    def debit(self, debt_amount):
        self.balance -= debt_amount
        print(debt_amount,"rupees debited from your account!")
        print("Your new balance is :",self.balance)
    
    def credit(self, credit_amount):
        self.balance += credit_amount
        print(credit_amount,"rupees credited to your account!")
        print("Your new balance is :",self.balance)

    def check_balance(self):
        print("Your current balance is ",self.balance)

customer1 = Account(123456, 120000)
customer1.credit(35000)
customer1.debit(15000)
customer1.check_balance()
    