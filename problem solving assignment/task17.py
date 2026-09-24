vowel_count=0
consonant_count=0
for i in range(5):
    name=input("Enter your name")
    marks=int(input("Enter your makrs:-")) 
    if marks>90:
        print("A")
    elif marks>70:
        print("B")
    elif marks>=35:
        print("C")
    elif marks<35:
        print("Fail")

       
    if name in "aeiouAEIUO":
            vowel_count+=1
    elif name not in "aeiouAEIOU":
            consonant_count+=1

    if vowel_count>consonant_count:
      print("Vowel Heavy")
    elif consonant_count>vowel_count:
        print('Consonant heavy')
    else:
      print("Tie")

    print(len(name))