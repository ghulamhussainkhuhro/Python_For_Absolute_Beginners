class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def show_num(self):
        print(self.real,"i + ",self.img,"j")
    
    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        Complex(newReal, newImg)
        return Complex(newReal, newImg)
    
num1 = Complex(1, 3)
num1.show_num()
num2 = Complex(4,6)
num2.show_num()

num3 = num1.add(num2) 
# num3 = num1 + num2 # This will lead to error TypeError: unsupported operand type(s) for +: 'Complex' and 'Complex'
# We can use dunder functions( functions with 2 underscores) to solve above error
num3.show_num()

# See Program116.py to observe changes


        