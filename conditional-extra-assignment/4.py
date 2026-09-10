a=int(input("Enter any numbers:-"))
b=int(input("Enter any numbers:-"))
c=int(input("Enter any numbers:-"))
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
elif c<a and c<b:
    print(c)
else:
    print("Enter valid value ")