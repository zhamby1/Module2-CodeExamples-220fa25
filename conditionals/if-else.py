#if else statements are dual alternative that assign a block of code to run when a statement evaluates to false
#else is a catch-all for any situation that the if does not meet
#if else to check if you accept the terms and conditions

terms_and_conditions = "yes"

if terms_and_conditions == "yes":
    print("You accepted the terms and condition.  Access Allowed")
else:
    print("You did NOT accept the terms and conditions.. Access Denied")


#checking to see if you are the age of majority (18 or older) to vote
age = int(input("Please enter your age "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
