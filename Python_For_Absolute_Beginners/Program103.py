class Person:
    # Private attribute
    __name = "Ghulam Hussain"

    # Private method
    
    def __print_Hello(self):
        print("Hello",self.__name,", How are you?")
    # Some method are private because we want that no any outside wntity can access them and only functions within class can access them
    
    def welcome(self):
        print("*****************************************")
        print("*\tThis is a welcome message\t*")
        print("*****************************************")
        self.__print_Hello()

p1 = Person()
p1.welcome()
# We cannot directly access __print_hello() or __name but by using them in a non private method we can access them.
