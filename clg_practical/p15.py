#Write a Python program to find average of numbers in a list.
items = [1,2,3,4,5,6]
sum =0
count = len(items)
for i in range(0,count):
    sum += items[i]
avg = sum / count
print("Average in list ",avg)