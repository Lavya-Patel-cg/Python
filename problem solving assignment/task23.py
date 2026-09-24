count_100000=0
count_50000=0
count_25000=0
count=0
employee_100000=0
employee_50000=0
employee_25000=0
employee=0  


for i in range(1,9):
    salary=int(input("Enter salay of {i} person:-"))
    if salary>100000:
        count_100000+=salary
        employee_100000+=1

        print("Executive")
    elif salary>50000:
        count_50000+=salary
        employee_50000+=1
        print("Senior")
    elif salary>=25000:
        count_25000+=salary
        employee_25000+=1
        print("Mid")
    elif salary<25000:
        count+=salary
        employee==1
        print("Junior")

total=count+count_25000+count_50000+count_100000
average_salary=total/8
print("Avearge salary of employees are:-",average_salary)
print("Employee in Executive category are:-", employee_100000)
print("Employee in Senior category are:-", employee_50000)
print("Employee in Mid category are :-", employee_25000)
print("Employee in Junior category are:-", employee)

