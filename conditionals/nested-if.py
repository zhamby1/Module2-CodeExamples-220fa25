#nested ifs work by having to meet multiple conditions through a series of if statements inside other if statements
#compound operators and elif statements will help avoid some nested if statements becasue they can become messy

#for instance we need to be 18 years and older and a us citizen to vote

age = int(input("Please give me your age "))
us_citizen = input("Are you a US citizen. Press y and enter for yes, n and enter for no ")

if age >= 18:
    if us_citizen == "y":
        print("You can vote")
    else:
        print("You cannot vote because you are not a US citizen")
else:
    print("You are not old enough to vote")