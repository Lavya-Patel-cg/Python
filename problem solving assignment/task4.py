password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False  
for i in password:
    if "A" <= i <= "Z":
        has_upper = True
    elif "a" <= i <= "z":
        has_lower = True
    elif "0" <= i <= "9":
        has_digit = True
    elif i in "!@#$%^&*_-=+~`/?><,.;:'": 
        has_special = True  

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong")

elif len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Medium")

elif len(password) >= 8 and has_upper and has_lower:
    print("Weak")

else:
    print("Very Weak")
                

