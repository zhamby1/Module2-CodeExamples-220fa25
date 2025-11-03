#or means only one must be true for the code to run

#lets use an example of a discounted movie ticket
#tickets at a theatre are mostly discounted if you a child or a senior citizen

ticket_price = 10.00
discount = 0.10

age = int(input("How old are you? "))
#in all compound conditions make sure that you are listing the full evaluation
#you cannot say if age <= 12 or >= 65  you have to use the variable twice
#we use the word or to compare the values

if age <= 12 or age >= 65:
    ticket_price = ticket_price - (ticket_price * discount)
    print("You are able to get a discount. Here is your ticket price:", ticket_price)
else:
    print("You do not get a discount.  Here is your ticket price:", ticket_price)