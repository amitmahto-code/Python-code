#write a python to print sum of n number using UDF
def sum(n):
    sum =0
    for i in range(1,n+1):
        sum+=i
    print(sum)
n = int(input("Enter number"))
sum(n)                                                  
     