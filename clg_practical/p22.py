''' write a python to calculate net salary where net salary = basic salary +hra+da-pf ,
hra is 10% of basic salary ,da is 50% of basic salary and pf is 20 % of the basic salary '''
basic_salary = float(input("Enter  your basic salary: "))
hra = basic_salary*0.10
da = basic_salary*0.50
pf = basic_salary*0.20
print("Net salary:= ",basic_salary+hra+da-pf)