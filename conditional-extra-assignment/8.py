a=int(input("Enter your marks:-"))
if a>100 or a<0:
    print("Invalid marks")
elif a>40:
    print("pass")
elif a<40:
    print("Fail")
else:
    print("enter valid marks")