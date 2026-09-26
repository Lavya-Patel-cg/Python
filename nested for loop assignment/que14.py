for i in range(0,10,2):
    for j in range(0,i+1,2):
        print(j, end=" ")
    print()  

    #OR
n=int(input("Enter any integer:-"))
for i in range(1,n+1):
    if i%2!=0:
     for j in range(i):
        if j%2==0:
         print(j,end=" ")
          
        
     print()    