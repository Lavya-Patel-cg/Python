marks1=int(input("Enter marks of 1st subject"))
marks2=int(input("Enter marks of 2nd subject"))
marks3=int(input("Enter marks of 3rd subject")) 
if marks1>100 or marks1<0:
    print("Invalid marks")
elif marks2>100 or marks2<0:
    print("Invalid marks")
elif marks3>100 or marks3<0:
    print("Invalid marks")
elif (marks1 or marks2 or marks3)<35:
    print("FAIL")



else:  
         Marks = print(((marks3 + marks2 + marks1)/3))
if  Marks>=75:

    print("Distinction")
elif Marks>=60:
    print("First Class")
elif Marks>=50:
    print("Second class")
elif Marks>=35:
    print("Pass")
else:
    print("Enter valid input")
    
