a=int(input("Enter any integer:-"))
if a<0:
    print('negative')
elif 0<=a<=10:
    print("number is between 0 to 10")
elif 11<=a<=50:
    print("number is between 11 to 50")
elif 51<=a<=100:
    print("number is between 51 to 100")
elif a>100:
    print("number is greater than 100")