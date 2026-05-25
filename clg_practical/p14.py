#Write a Python program to sum all the items in a list.
items = [1,3,5,7,8,9]
sum = 0
for i in range(0,len(items)):
    sum += items[i]
print(sum)