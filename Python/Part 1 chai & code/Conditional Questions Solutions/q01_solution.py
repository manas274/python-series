# age = input("provide me an age") OR
# age = int(input("provide me an age")) OR
# age_in_int = int(age)   OR

age = 65
if age < 13:
    print("Child")  # this is part of if becuz indentation of 4 spaces.
# print("chai") ... this will be printed if condition is true or not becuz no indentation.

elif age < 20:
    print("Teenager")
    
elif age < 60:
    print("Adult")
    
else:
    print("Senior")