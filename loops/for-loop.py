#for loop repeats code a certain number of times

#python is a little weird when it comes to for loops.  There are several ways to do it, but in other languages a for loop looks very similar to this:

# for(int i = 0; i < 10; i = i + 1)
#i is just a short hand for iterator value
#iterator is the values that keeps up with the current loop number/value
#iteration means to go through a loop or cycle

#what python does differently is it uses a for in loop followed by a range function that takes care of our iterator values
#for in loop - for something in something.  aka for iterator value in number of loops
#syntax for a for in loop would be - for i in range(start,stop,increment)
number = 5
for i in range(0,number,1):
    print(i)

print("**********************")

#countdown by using negative values
countdown = 0
for i in range(10,0,-1):
    print(i)

print("****************")
#we can also count by other values than 2
for i in range(0,40,2):
    print(i)