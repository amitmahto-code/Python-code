# Break statement 

for i in range(100):
    if i==3:
        break #exit right now loop
    print(i)
print("\n")
#continue statement 

for i in range(10):
    if(i==3):
        continue #skip that iteration 
    print(i)

#pass statement 

print("\n")
l=[1,2,3,4]
for items in l:
    pass
i=1
while i<5:
    print(i)
    i+=1