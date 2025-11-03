#compound conditions and their operators allow for multiple conditions inline with our if statements
#there are three types of compound conditions

#and - both conditions must be true for the block of code to run
#or - only one condition must be true for the block of code to run
#not - flips the resulting boolean to it's opposite

#truth tables
# https://www.realdigital.org/doc/e127ebfa82dbc904b5c0dac5d1adce8e

#and condition - lets take the voting program in the nested if file and use a compound condition instead


age = int(input("Please give me your age "))
us_citizen = input("Are you a US citizen. Press y and enter for yes, n and enter for no ")

#to use and in python just type the word and
if age >= 18 and us_citizen == "y":
    print("You can vote")
else:
    print("You cannot vote")