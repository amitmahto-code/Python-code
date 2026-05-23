# write a python program that accepts input as marks of 3 subject for each student.
# display total marks, percentage and grade (if per >70 then grade DIST ,per>60 then grade FIRST, per >50 then grade SECOND , per >40 then grade pass)
#each student
m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

total_marks = m1+m2+m3

per = (total_marks/300)*100
if(per >= 70):
    print(f"Garde :Dist, per: {per}")
elif(per >= 60 and per <70):
    print(f"Garde :First, per: {per}")
elif(per >= 50 and per < 60):
    print(f"Garde :Second, per: {per}")
elif(per >= 40 and per < 50):
    print(f"Garde :Pass, per: {per}")
else:
    print(F"Grade :Fail, per: {per}")
