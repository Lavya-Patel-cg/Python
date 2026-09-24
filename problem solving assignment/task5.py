
for i in range(1,3):
    char=input("Enter string ")
    if len(char)>6:
        print("Long")
    elif len(char)>4:
        print("Medium")
    elif len(char)<=3:
        print("Short")