marks = int(input("Enter obtained marks: "))

if marks >= 90 and marks <= 100:
    print("Grade = A")
       
elif marks >= 80 and marks <= 89:
    print("Grade = B")
       
elif marks >= 70 and marks <= 79:
    print("Grade = C")
       
elif marks >= 60 and marks <= 69:
    print("Grade = D")
       
       
else:
    print("Grade = F")
       
       
# Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).