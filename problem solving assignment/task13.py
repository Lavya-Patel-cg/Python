bill=0
for i in range(6):
    usage=int(input("Enter units of electricity used:-"))
    if usage>400:
        bill= bill + (100*5) + (100*7) + (200*10) + (usage*15) 
        print("Amount to be paid", bill)
    elif usage>200:
        bill = bill + (100*5) + (100*7) + (usage*10)
        print("Amount to be paid", bill)
    elif usage>100:
        bill=bill + (100*5) + (usage*7)
        print("Amount to be paid:-", bill)
    elif usage>0:
        bill=bill + (usage*5)
        print("Amount to be paid:-", bill)


    if bill>3000:
          print("High")
    elif bill>=1000:
            print("Medium")
    elif bill<1000:
               print("Low")         

