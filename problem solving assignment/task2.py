Failed_Students=0
Excellent_students=0
Good_students=0
Pass_students=0
for i in range(1,11):
    marks=int(input((f"Enter marks of student number {i}:-")))
    if marks<35:
        Failed_Students+=1
        print("Fail")
    elif marks>75:
        Excellent_students+=1
        print("Excellent")
    elif marks>50:
        Good_students+=1
        print("Good")
    elif marks>=35:
        Pass_students+=1 
        print("Pass") 

print("Number of failed students are ",Failed_Students)
print("Number of Excellent students are ",Excellent_students)
print("Number of Good  students are ",Good_students)
print("Number of Pass students are ",Pass_students)