password=input("Enter your password:-")
dot_count=0
at_the_rate_count=0
digit_count=0
special_character=0
password_pattern=0
for i in password: 
    if i == ".":
        dot_count+=1
    elif i == "@":
        at_the_rate_count+=1 
    elif "0"<=i<="9":
        digit_count+=1
    elif i=="!#$%^&():;',<>/?]}[{":
        special_character+=1
    else:
        password_pattern+=1



if dot_count> at_the_rate_count and digit_count and special_character and password_pattern:
    print("Weak")
elif special_character> at_the_rate_count and digit_count and dot_count and password_pattern:
    print("Strong")
elif digit_count> special_character and at_the_rate_count and dot_count and password_pattern:
    print("Medium")
elif at_the_rate_count> dot_count and special_character and digit_count and password_pattern:
    print("Weak") 