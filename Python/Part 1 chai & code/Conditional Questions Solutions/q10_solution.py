Pet = str(input("Which pet: "))
Age = int(input( "Age: "))

if Pet == 'Dog' and Age < 2:
    print("Recommended food is Puppy Food")
    
elif Pet == 'Cat' and Age > 5:
    print("Recommended food is Senior Cat Food")