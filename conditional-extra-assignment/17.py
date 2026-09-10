c=int(input("Enter 1 for addition \n 2 for subtraction \n 3 for multiply\n 4 for division \n 5 for floor division:-"))
if c==1 or c==2 or c==3 or c==4 or c==5: #Used to save time if user enters a value other than 1 to 5


 a=int(input("Enter any integer:-"))
 b=int(input("Enter another integer:-"))

 if c == 1:
    print(a+b)
 elif c == 2:
    print(a-b)
 elif c == 3:
    print(a*b)
 elif c == 4 and b!=0:
    print(a/b)
 elif c == 5:
    print(a//b)
else:
    print("Enter a valid vaue")
