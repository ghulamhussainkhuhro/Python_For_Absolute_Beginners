# lists and dictionaries are mutable hence cannot be stored in a set
# V.N.B : Set itself is mutable but its elements are immutable

collection = set()
collection.add("Hi")
collection.add("Ghulam Hussain")
collection.add(19)
collection.add(69350.873)
# collection.add([1,2,3]) # Error! TypeError: unhashable type: 'list'
collection.add((1,2,"BJ")) #tuple
dict = {
    "name" : "Bhopendra Jogi",
    "places_visited_in_US" : "too many",
    "names_of_visited_places" : "Bhopendra Jogi" 
} 
print("Type:",type(dict))
# this is a dictionary names dict as I have already demonstrated that adding list in a set leads to error 
# down there you will see that adding dictionaries in a set also leads us to errors

# collection.add(dict) TypeError: unhashable type: 'dict'


#Removing an element in a set
# collection.remove(element) removes the element of set which was entered in ()

collection2 = {1,2,2,3,1,2}
print("Type:",type(collection2))
print("Length of set:",len(collection2))
print("Before removing element '2':",collection2)
collection2.remove(2)
print("After removing element '2':",collection2)

# collection2.clear() clears/removes all the elements of a set 

collection2.clear()
print("After calling clear():",collection2)

# collection2.pop() removes a random element from a set
collection3 = {"a","s","d","f","j","k","l"}
print("Type:",type(collection3))
print("Length of set:",len(collection3))
print("Before calling pop():",collection3)
collection3.pop()
print("1st call to pop():",collection3)
collection3.pop()
print("2nd call to pop():",collection3)
collection3.pop()
print("3rd call to pop():",collection3)

# you will see than on each call it will remove a random value + print in random order

# collection2.pop()
                  


