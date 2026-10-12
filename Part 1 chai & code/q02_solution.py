age = int(input("Enter your age: "))
day = input("Enter the day: ")


if day == "wednesday" and age < 18:
    print("Ticket price = 6$")

elif day == "wednesday" and age >= 18:
    print("Ticket price = 10$")

elif age < 18:
    print("Ticket price = 8$")
    

else:
    print("Ticket price = 12$")
    

    
    
    
