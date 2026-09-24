for i in range(3):
    for j in range(3):
        print(j, end="")
    print() 

    if i%2==0:
        print("even")
        if j%2==0:
            print("Even")
        elif j%2!=0:
            print("Odd")
    elif i%2!=0:
        print("Odd")        
        
      