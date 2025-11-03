#we can also use loops as accumulators (ie keep up with a running total)
#this program averages numbers

# average = sum / number of values
sum = 0
average = 0

how_many_numbers = int(input("Please enter the amount of numbers you wish to average "))

#we can use a for loop or a while loop for this...but for loop make sense because we are interating a certain number of time (count controlled)
for i in range(0,how_many_numbers,1):
    number = float(input("Please enter the number you wish to average "))
    #accumulator
    sum = sum + number

print("Your total sum is", sum)
average = sum / how_many_numbers
print("Your average is", average)