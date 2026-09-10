username=input("Enter your  username:-")
password=input("Enter your password:-")
if username=="admin" and password=="python123":
    print("Login successful")
elif username=="admin" and password!="python123":
    print("Password not correct")
elif username!="admin" and password=="python123":
    print("Username not correct")