# write a programa to find whether a given number us prime or not.
n = int(input("Enter number: "))
for i in range(2,n):
    if n % i == 0:
        print("Number is not prime ")
        break
else:
    print("number is prime number")