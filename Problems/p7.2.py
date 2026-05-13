""" write a program to greet all the person names stored in a list 'l' and which starts with s
l=["Harry", "Sohan", "sachin", "Rahual"]"""

l=["Harry", "Sohan", "Sachin", "Rahual"]

for item in l:
    if(item.startswith("S")):
        print(f"hello {item}")