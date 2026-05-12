# write a program which finds out whether a given name is present in a list or not
l1=["Amit", "Kunal", "Gaurav", "Sunita", "Pooja"]
name = input("Enter your name: ")
if(name in l1):
    print("yes this is present in list ",name)
else:
    print("not this is not present in list ",name)
    