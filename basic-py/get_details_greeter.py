#Simple Function to get details
def get_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    course = input("Enter your course: ")
    return name, age, course

#Main
print ("\n========================================[SIMPLE GREETER PROGRAM]========================================") #Heading
name, age, course = get_details() #Function Call
print("\nHi "+name+"! I see that you are already "+age+" years old. Goodluck pursuing "+course+"!\n") #Greeter



