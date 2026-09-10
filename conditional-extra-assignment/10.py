age=int(input("Enter your age:-"))
if age<0:
    print("invalid age")
elif  age<18 :
    print("Can't Vote")
elif age>18 or age>120:
    print("Can Vote")
else: print("Enter a valid age")