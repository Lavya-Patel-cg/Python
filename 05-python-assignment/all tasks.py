#creating a string
name="Lavya"
city_name="Ahmedabad"
fav_programming_lang="""Python"""
message="hellooo everyone"
print(name)
print(city_name)
print(fav_programming_lang)
print(message)



#empty string
a=""
print(a)
print(len(a))
print(type(a))


#string information
a="Python Programming"
print(a[:])
print(len(a))
print(a[0])
print(a[-1])
print(a[2])
print(a[-2])


#positive indexing
a="Programming"
print(a[0])
print(a[1])
print(a[4])
print(a[-1])


#negative indexing
a="Programming"
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-11])


#indexing challenge
a="lavya patel"
print(a[0])
print(a[-1])
print(a[6])



#basic slicing
a="Python Programming"
print(a[0:6])
print(a[7:17])
print(a[:])
print(a[:5])
print(a[-5:])


#slicing with step
a="ABCDEFGHIJKL"
print(a[::2])
print(a[::3])
print(a[1:8:2])
print(a[::-1])


#slicing with negative indexes
a="Python Programming"
print(a[-5:])
print(a[-10:])
print(a[::-1])



#slicing challenge
a="Python Programming"
print(a[:4])
print(a[-3:])
print(a[::2])
print(a[::-1])
print(a[1:-2])


#length
a="hello"
b="hello world"
c="hello how are you all "
print(len(a))
print(len(b))
print(len(c))


#task 12
text = "Python Programming"
print(len(text)-1)


#concatenation
first_name="Lavya"
last_name="patel"
print(first_name + ' ' + last_name)


#sentence creation
name="lavya"
age=17
age=str(age)
city_name="Ahmedabad"
fav_programming_lang="Python"
print(name + " " + age + " " + city_name + " " + fav_programming_lang)


#string and integer
a=19
a=str(a)
b="age"
print(a+ " " +b)


#string repetation
a="@"
print(a*3)
print(a*5)
print(a*10)
#pattern
a="*" * 10
print(a)


#case conversion
a="python programming language"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())


# case insensitive comparison
a="Python"
b="python"
print(a==b)


# task20
text="Python is a programming language"
print("Python" in text)
print("programming" in text)
print("Java" in text)
print("language" in text)


#task21
text="Python is a programming language"
print(text.find("Python"))
print(text.find("programming"))
print(text.find("Java"))
print(text.find("language"))


#task22
text="Python is a programming language"
print(text.index("Python"))
print(text.index("programming"))
print(text.index("Java"))
print(text.index("language"))


#task23
a="banana"
print(a.count("a"))
print(a.count("b"))
print(a.count("n"))



#task24
filename = "student_notes.pdf"
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))
print(filename.startswith("student"))



#task25
text = "I am learning Java"
new_text = text.replace("Java", "Python")
print(new_text)



#task26
text = "apple apple apple"
print(text.replace("apple", "mango"))



#task27
text ="apple"
print(text.replace("apple", "mango"))


#task28



#task29
text = "   Python Programming   "
print(text.strip()) # Removes both leading and trailing spaces
print(text.lstrip()) # Removes leading spaces
print(text.rstrip()) # Removes trailing spaces
#task30


#task31
text="Python is easy to learn"
print(text.split())
#task32
text = "apple,banana,mango,orange"

print(type(text.split(",")))


#task33
words = ["Python", "is", "easy"]
print(" ".join(words))


#task34
text = "Python is easy"
print("-".join(text.split()))


#task35
name ="Lavya"
age=18
city="Ahmedabad"
print(f"My name is {name} and I am {age} years old. I live in {city}.")
#task36
a = 10
b = 20
print(f"The sum of {a} and {b} is {a+b}.")
#task37 
text = "Python"
print(text[20])  #index out of range error

text = "Python"
text[0] = "J" #typeerror

age = 20
print("Age: " + age) #typeerror

text = "Python"
print(text.index("Java")) #valueeror