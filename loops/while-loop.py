#loops are also part the control structures category.  They repeat code until a condition is met.
#loop main goal is to repeat code until you do not want it repeated
#two types of loops - while and for

#while loop - is a loop that repeats code until a specific condition is met, often using a flag or sentinel value to break the loop
#for loop - is similar to a while loop but repeates code a certain number of times.  This is called count controlled and is controlled by a counter variable or iterable.

#while loops are usually broken by a flag value that is changed inside the block of code attached to the loop

#flag/sentinel value
keep_going = "y"

#make a commission program to check sales and sales commissions...breaks when the user is done entering data
#we use the same comparison (relational) operators that conditionals use..the while condition :

while keep_going == "y":
    sales = float(input("Give me your sales for the month "))
    com_rate = float(input("What is your commission rate in decimal form? "))
    total_earned = sales * com_rate
    print("You have earned", total_earned, "this month.")
    keep_going = input("Do you wish to run again? Press y and enter for yes or n and enter for no")

print("Thanks for using our program")