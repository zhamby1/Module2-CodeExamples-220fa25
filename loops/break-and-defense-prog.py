#sometimes we want to use a loop to check for certain conditions in order to defensivly program
#what I mean by that is not moving on in a program until a condition, or not accepting something we given wrong input
#we can use flag values and other techniques to help us do this

#break is a great way to break a loop without worrying about flag value
#it allows us to just break out of a loop whenever we use the keyword

#to use break we often just say while True

while True:
    accept = input("Do you accept the terms and conditions..Press y and enter for yes ")
    #we can use conditions to go down a certain path to see when we would break out of a loop
    if accept == "y":
        print("Thanks for accepting")
        break
    else:
        print("You cannot use this program until you accept the T&C. Try again")


print("Access Granted")