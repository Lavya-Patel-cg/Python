number=str(input("Enter any number:-"))
count=0
Count=0
for i in number:
    if int(i)%2==0:
       count=count+1
    elif int(i)%2!=0:
        Count=Count+1 

if count>Count:
    print("Even")
elif Count>count: 
    print("Odd")
else:
    print("Equal")         
        
   

