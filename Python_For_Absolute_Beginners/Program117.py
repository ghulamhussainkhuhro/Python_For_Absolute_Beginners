# Create a class called order which store items nd its price 
# Use dundur function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2

class Order:

    def __init__(self, item, price):
        self.item =item
        self.price = price
    
    def __gt__(self, order2):
        return self.price >  order2.price

order1 = Order("Chips", 30)
order2 = Order("Tea",60)

print(order1 > order2)
        