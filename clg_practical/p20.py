#Write a python program to check if an item exists in a tuple or not
item = (1,3,4,3)
n =int(input("Enter number: "))
if n in item:
    print(f"yea {n} is in tuple")
else:
    print(f"{n} not in tuple")
