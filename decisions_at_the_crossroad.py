#DECISIONS AT THE CROSSROAD
#TASK 1
#Buggy Code

# number = input("Enter a number: ")

# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")

    #FIRST attempt at correcting. Did not work. Misuse of 'else' 

# number = int(input("Enter a number: "))      #fix integer issue

# if number > 0:
#     print("The number is positive.")
# elif number == 0:       # '==' issue. Prompted by VS Code
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")

    #SECOND attempt. Works fine

number = int(input("Enter a whole number: "))     #added 'whole number' for direction

if number > 0:
    print("The number is positive.")
elif number == 0:       
    print("The number is zero.")
else:
    print("The number is negative.")