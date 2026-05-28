'''Write a Python program that performs the following:
1. Sort the list
2. Display total of the all elements of the list.
3. Display last element of the list.'''

itmes =[1,3,5,2,7]
total = 0
itmes.sort()
print("Sorted list ",itmes)
for i in range(0,len(itmes)):
    total+=itmes[i]
print("total of list",total)
print("last element of list",itmes[-1])