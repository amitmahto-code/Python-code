#write a recurcive funtion to calculate the sum of first n natural number
def sum(n):
    
    if  n==1:
        return 1
    
    return n + sum(n-1)
n =int(input("Enter number: "))
print("Total: ",sum(n))