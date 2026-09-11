a=float(input("Enter units of electricity used:-"))
if a<=100:
    amount=a*5
    print("Bill:-", amount)
elif a<=200:
    amount=100*5 + ((a-100)*7)
    print("Bill:-", amount)
elif a>200:
    amount=100*5 + 100*7  + (a-200)*10
    print("Total bill:-",amount) 
else:
    print("Enter valid Units of electricity")