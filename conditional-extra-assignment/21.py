a=int(input("Enter length of 1stside"))
b=int(input("Enter length of 2nd side"))
c=int(input("Enter length of 3rd side"))
if a==b==c:
    print("Equilateral triangle")
elif a==b!=c or a==c!=b or b==c!=a:
    print("Isosceles triangle")
elif a!=b!=c:
    print("Scalene triangle")
    