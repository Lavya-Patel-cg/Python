a=int(input("Enter any integer:-"))
if a%2==0 and a>0:
    print("Even&Positive")
elif a%2!=0 and a>0:
 print("Positive&Odd")
elif a%2==0 and a<0:
   print("Negative&Even")
elif a%2!=0 and a<0:
   print("Negative&Odd")
else:
   print("Enter a valid integer")
