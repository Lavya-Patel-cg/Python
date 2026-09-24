a=input("Enter any string:-")
for i in a:
    vowel_count=0
    consonant_count=0
    if i in "aeiouAEIOU":
        vowel_count+=1
    elif i in "qwrtyplkjhgfdszxcvbnmQWRTYPLKJHGFDSZXCVBNM":
        consonant_count+=1
if vowel_count>consonant_count:
    print("Vowel Heavy") 
elif consonant_count>vowel_count:
    print("Consonant Heavy")
else:print("Balanced")        