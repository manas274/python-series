Password = str(input("Create your password: "))

if len(Password) < 6  :
    print("Weak password")
    
elif 6 <= len(Password) <= 10  :
    print("Medium password")
    
else:
    print("Strong password")