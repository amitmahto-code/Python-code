# Write a program to find whether a given username contains less than 10 characters or not

username = input("Enter name: ")
size = len(username)
if(size<10 ):
    print("yes less than 10 characters: ",size)
else:
    print("Not more than 10 characters: ",size)
