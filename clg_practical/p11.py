# write a python program to create choic based menu for culculator operation
n = int(input("Enter number: "))
operater = input("Enter operater: ")
n1 = int(input("Enter second number: "))

for i in range(1):
    if operater == '+':
        sum = n+n1
        print(sum)
        break
    elif operater == '*':
        product = n1*n
        print(product)
        break
    else:
        print("Invaild")
