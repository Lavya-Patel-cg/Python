a=int(input("Enter any integer:-"))
if a%3==0 and a%7==0:
    print("It is divisible by both 3 and 7")
elif a%3==0:
    print("It is divisible only by 3")
elif a%7==0:
    print("It is divisible only by 7")
elif a%3!=0 and a%7!=0:
    print("It is not divisible by 3 and 7")
else:print("Enter valid value ")