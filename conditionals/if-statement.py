#if statement is known as a single alternative.  One branching bath...the if
#conditionals basically allow us to create branching paths on conditionals
# relational operators - > < <= >= == !=

#an if statement does not need an else to work...there are many cases in which you may just want to use an if statement
a = 7
b = 7

#if statements in python do not require the condition in ()
#python uses braces mainly for objects..so to make an if statment and it's body we use : followed by indentation
#if the condition is true, then the block of code attached to the condition runs
#if the evaluation is false, the if statement gets skipped - short circuit evaluation
# we use == for comparisons and = to assign value
if a == b:
    print("These are equal")


#when we are utilizing evaluations or conditionals, we are getting a boolean as a result
#boolean are true/false values...you can use them in other parts of your program

mybool_true = True
mybool_false = False

#! in python denotes not and we use often for not equals.  This checks the opposite value result of an evaluation
#if something is true, flip it to false and vice versa

x = 50
y = 22

if x != y:
    print("These values are not equal")