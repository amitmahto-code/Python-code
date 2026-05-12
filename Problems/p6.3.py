#A spam comment is defined as a text containing following keywords 
# "Make a lot of money","Buy now", "Subscribe this", "click this",. write a program to detect these spams.

p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "click this"
massage = input("Enter comment: ")

if(p1 in massage  or p2 in massage  or p3 in massage  or  p4 in massage ):
    print("Alert this spam")
else:
    print("vaild comment")