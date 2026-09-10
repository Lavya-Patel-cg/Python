a=int(input("Enter amount:-"))
if a<500 :
    print(a)
elif 500<=a<999:
   
    bill=( a - a*0.05)
    print("Amount to be paid:-",bill)
    print(f"Original price{a} , discount=5%")
elif 1000<=a<1999:
    bill=(a -a*0.1)
    print("Amount to be paid:-", bill)
    print(f"Original price{a} , discount=10%")
elif 2000<=a<4999:
    bill=(a - a*0.15)
    print("Amount to be paid:-", bill)
    print(f"Original price{a} , discount=15%")
elif a>=5000:
    bill=(a - a*0.2)

    print("Amount to be paid:-", bill)
    print(f"Original price{a} , discount=20%")
else:
    print("Invalid input")
    