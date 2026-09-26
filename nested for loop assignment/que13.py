#for i in range(1,10,2):
 #   for j in range(1,i+1,2):
  #      print(j, end=" ")
   # print()  

    #0R
    # for i in range(1,6):
    #    for j in range(1,i+1):
    #         print(j*2-1, end=" ")
    #    print() 
   
    # 0R
n=int(input("Enter any integer:-"))
for i in range(1,n+1):
    if i%2==0:
     for j in range(i):
        if j%2!=0:
         print(j,end="")
          
        
     print()          
   
       
      