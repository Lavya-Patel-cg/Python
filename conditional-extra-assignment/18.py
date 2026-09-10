temp=int(input("Enter temperature near you:- "))
if temp<0:
    print("Freezing")
elif temp>=15:
    print("Very Cold")
elif temp>=25:
    print("Cold")
elif temp>=35:
    print("Normal")
elif temp>35:
    print("very hot ")
elif temp>50:
    print("Enter a valid temperature")