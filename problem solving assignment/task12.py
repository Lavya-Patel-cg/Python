vowel=0
consonant=0
a=input("Enter any string:-")
for i in a:
    if i in "aeiou":
        vowel+=1
    elif i in "qwrtyplkjhgfdszxcvbnm":
        consonant+=1
if vowel>consonant:
        print("Vowel Wins")
elif consonant>vowel:
        print("Consonant Wins")
else:print("Tie")      
   
  
   
