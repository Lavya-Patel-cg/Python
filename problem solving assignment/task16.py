password=input("Enter your password:-")
uppercase=0
lowercase=0
digit_count=0
special_character=0
for i in password: 
    if "A"<=i<="Z":
        uppercase+=1
    elif "a"<=i<="z":
        lowercase+=1 
    elif "0"<=i<="9":
        digit_count+=1
    else:
        special_character+=1
total=uppercase+lowercase+digit_count+special_character
print("Percentage uppercase is:- ", (uppercase/total)) 
print("Percentage lowercase is :-", (lowercase/total))
print("Percentage digits is:-", (digit_count/total))
print("Percentage special character is :-", (special_character/total)) 

if uppercase> lowercase and digit_count and special_character:
    print("Weak")
elif special_character> lowercase and digit_count and uppercase:
    print("Strong")
elif digit_count> special_character and lowercase and uppercase:
    print("Medium")
elif lowercase> uppercase and special_character and digit_count:
    print("Weak") 
    