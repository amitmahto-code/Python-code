#write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject
# to pass. Assume 3 subject and take marks as an input from the user

m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
per =((m1 + m2 + m3 )/300)*100
if( m1>=33 and m2>=33 and m3>=33 and per>=40):
    print(" you are pass",per)
else:
    print("Try your next timr ",per)