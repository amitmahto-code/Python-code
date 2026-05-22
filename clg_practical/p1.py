#write a python program to display reverse number
# eg. I/P = 1234 O/P =4321

n = int(input("Enter number: "))
rev = 0
while n > 0:
    temp = n % 10
    rev = (rev * 10)+temp
    n = n // 10
print(rev)  