string=input("Enter any string:-") 


for i in string:
   print(i)  
   print("Index position of this Character is ",string.index(i)) 
   if string.index(i)%2==0 and i in "aeiou":
      print("Vowel")
      print("Even")
   elif string.index(i)%2==0 and i not in "aeiou":
      print("Consonant")
      print("Even") 
   elif string.index(i)%2==0 and "0"<=i<="9":
      print("Even")
      print("Digit")
   elif string.index(i)%2==0:
      print("Even")
      print("Special Characters") 
   elif string.index(i)%2!=0 and i in "aeiou":
      print("Vowel")
      print("Odd") 
   elif string.index(i)%2!=0 and i not in "aeiou":
            print("Consonant") 
            print("Odd")       
   elif string.index(i)%2!=0 and "0"<=i<="9":
          print("Odd")
          print("Digit")
   elif string.index(i)%2!=0:
       print("Odd")
       print("Special") 
      

      
    