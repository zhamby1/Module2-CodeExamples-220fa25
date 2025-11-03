#not - flips true to false and flips false to true

x = 10

#nots are often used with other compound conditions to get a result.
#for instance I want to see x does not equal 11 or 10

if not(x == 10 or x == 11):
    print("X is not equal to 10 or 11")
else:
    print("X is equal to 10 or 11")