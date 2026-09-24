vowel=0
consonant=0
digit=0
Special_character=0
string=input("Enter any string").lower()
for i in string:
    if i == "aeiou":
        vowel+=2
        
    elif "a"<=i<="z":
        consonant+=1
       
    elif "0"<=i<="9":
        digit+=3
       
    else: 
        Special_character+=4
total=vowel+consonant+digit+Special_character
print(total)          
    