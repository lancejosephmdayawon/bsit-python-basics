#Surname_Seat1.pdf
#1.00  and 1.25 Excellent
#1.5 and 1.75 Very good
#2.00 - 2.25 Good
#2.5 -2.75 Satisfactory
#3.0 Passed
#lower than 3.00 Failed

print ("\n=============[Numerical Grade Remarks]=============\n")

grade = float(input("Enter numerical grade: "))

if 1.00 <= grade <= 1.25:
    print(f"Grade: {grade}\nRemarks: Excellent")
elif 1.50 <= grade <= 1.75:
    print(f"Grade: {grade}\nRemarks: Very good")
elif 2.00 <= grade <= 2.25:
    print(f"Grade: {grade}\nRemarks: Good")
elif 2.50 <= grade <= 2.75:
    print(f"Grade: {grade}\nRemarks: Satisfactory")
elif grade == 3.00:
    print(f"Grade: {grade}\nRemarks: Passed")
elif 3.00 < grade <= 5.00:
    print(f"Grade: {grade}\nRemarks: Failed")
else:
    print("Invalid grade entered.")