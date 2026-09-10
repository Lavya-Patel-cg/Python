a=int(input("Enter any integer:-"))
if a%5==0 and a%11==0:
    print("It is divisible by both 5 and 11")
elif a%5==0:
    print("It is divisible only by 5")
elif a%11==0:
    print("It is divisible only by 11")
elif a%5!=0 and a%11!=0:
    print("It is not divisible by 5 and 11")
else:print("Enter valid value ")