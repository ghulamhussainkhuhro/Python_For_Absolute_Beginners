# WAP to ask the user to enter names of their 3 favourite dishes and store them in a list
fav_dishes = []
fav_dish1 = input( "Enter your 1st most favourite dish: ")
fav_dish2 = input("Enter your 2nd most favourite dish: ")
fav_dish3 = input("Enter your 3rd most favourite dish: ")

fav_dishes.append(fav_dish1)
fav_dishes.append(fav_dish2)
fav_dishes.append(fav_dish3)

print("Your choices stored in a list!")

print(fav_dishes)

#2nd Method

movies = []
mov = input("Enter 1st movie : ")
movies.append(mov)
mov = input("Enter 2nd movie : ")
movies.append(mov)
mov = input("Enter 3rd movie : ")
movies.append(mov)

print("Movies stored in a list :")
print(movies)

#3rd method:

movie = []
movie.append(input("Enter 1st movie : "))
movie.append(input("Enter 2nd movie : "))
movie.append(input("Enter 3rd movie : "))

print("Movies stored in a list :")
print(movie)
