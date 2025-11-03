#else-if statements are multi alternative and can have more than two branching paths
#usually deals with ranges or with having multiple conditions to check
#to do this in python we use else-if statements aka elif statements in python

#python does not have a switch case structure..so anything with a switch-case you would use elif

#below is an example of converting a numerical test score to a letter graded score
#ie A - 90-100   B - 80-89    C - 70-79  etc...

number_grade = 82
letter_grade = ""

if number_grade >= 90:
    letter_grade = "A"

#else-if use the elif keyword to check conditions
#well 80 is greater than 70 or 60...why does my letter grade not change to C or D?
#short-circuit evaluation
#as soon as a condition is met in a elif statement, it exits or skips the rest of the elif statements
elif number_grade >= 80:
    letter_grade = "B"

elif number_grade >= 70:
    letter_grade = "C"

elif number_grade >= 60:
    letter_grade = "D"

else:
    letter_grade = "F"

print("Your letter grade is", letter_grade)

