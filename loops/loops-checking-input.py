#we want to check your age, and you have to give us a numerical value.  You cannot give us a string


while True:
    age = input("What is your age? ")
    #isdigit() checks to see if a value is a number
    if age.isdigit():
        age_converted = int(age)
        print("Your are",age_converted,"years old")
        break
    else:
        print("Invalid input...please enter a number")


print("Thanks for using our program")