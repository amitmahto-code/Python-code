# write a python program to find factorial of a number
n = int(input("Enter number: "))
product = 1
for i in range(1,n+1):
    product = product * i
print("Factorial of number:",product)