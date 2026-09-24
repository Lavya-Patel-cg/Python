n=int(input("Enter any integer:-"))
for i in range(1,n+1):
    for j in range(n):
       print(i, end="")   
    print() 
if n%5==0:
    print("F")
elif n%2==0:
    print("E")    
    
   
elif n%2!=0:
    print("O")
    
   
