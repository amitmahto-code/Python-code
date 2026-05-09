# create an empty dictionary.Allow 4 friends to enter thier favorite language as values and
# use key as their names. Assume that the names are unique 

dist ={}

name = input("enter user name: ")
lang = input("Enter language: ")
dist.update({name:lang})

name = input("enter user name: ")
lang = input("Enter language: ")
dist.update({name:lang})

name = input("enter user name: ")
lang = input("Enter language: ")
dist.update({name:lang})

name = input("enter user name: ")
lang = input("Enter language: ")
dist.update({name:lang})

print(dist)