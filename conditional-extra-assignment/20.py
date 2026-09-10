a=int(input("Enter length of 1stside"))
b=int(input("Enter length of 2nd side"))
c=int(input("Enter length of 3rd side"))
if a+b>c : 
    print("It can form a triangle")
elif a+c>b:
        print("It can form a triangle")
elif b+c>a:
            print("It can form a triangle")
else:
        print("It cannot form a triangle")