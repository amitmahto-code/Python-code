#write a program to find thr greatest of four number enterd by the user

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1 > num2 and num1>num3 and num1>num4):
    print("Greatest number is n1: ",num1)
elif(num2 > num1 and num2>num3 and num2>num4):
    print("Greatest number is n2: ",num2)
elif(num3 > num1 and num3>num2 and num3>num4):
    print("Greatest number is n3: ",num3)
else:
    print("Greatest number is n4: ",num4)
