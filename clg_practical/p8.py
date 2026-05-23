# write a python to check if the number is an armstrong number is not
n = int(input("Enter number: "))
temp = n
product =0
while n>0:
    remainder = n % 10
    product =(remainder * remainder * remainder )+product
    n = n//10
if temp == product:
    print("yes armstorng number: ",product)
else:
    print("Not armstrong number: ",product)
