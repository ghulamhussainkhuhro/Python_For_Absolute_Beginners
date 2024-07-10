# Conceptual Private methods and attributes 
"""
Private methods and attributes are meant to be used only within the class and
are not accessible from outside the class 

__ by writing 2 underscores we can make attribute private

"""

class Account:

    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # account password created as private cannot be accessed outside the class directly

c1 = Account(123456, "dsafjg")
print("Account number :", c1.acc_no)
# print("Account password :", c1.__acc_pass) # AttributeError: 'Account' object has no attribute '__acc_pass

