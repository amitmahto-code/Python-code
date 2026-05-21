# write a program to calculate the factorial of a given number using for loop

n = int(input("Enter number: "))
product = 1
for i in range(1,n+1):
    product=product*i
print(f"foctorial of {n} is {product} ")