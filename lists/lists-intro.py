#data structures define how data is stored and organized outside of normal (primitive) data types (ie float string int)
#they contain multiple pieces of data and are organized based on the type of data structure you are using
#pythons simplist data structure is known as a lit
#this is similar to an array in other languages, with a few differences
#lists are dynamic in size (it is not fixed and can be virtually any size as long as you have the memory)
#lists can contain multiple data types inside (don't do this)
#lists are mutable - they can change after they are created, and items inside can be added, deleted or modified

#to create a list - syntax
#nameoflist = []
#a list can also be initialized as empty or with values already inside
#values are separated by a ,
names = []
test_scores = [100,99,85,54,95]

#to modify or "grab" items from a list, we have to know about indexes (position)
#an index is a location within the list that points to data values
#we have to use an index because each individual value does not have a variable name
#index in python start at 0, in the above example that means that index 0 - 100 , index 1 - 99, index 2 - 85, etc...

#print 100
print(test_scores[0])
#print 99
print(test_scores[1])

#one of the biggest advantages to a list is the ability to loop, search, and process data in a list
#if we need to display all the items in a list, for example, we could do the horrible task of printing each index one at a time.
#instead, what we normally do is loop through the list and grab items / elements

#for in loop - counts the number of items and loops through the list that same number of times
#syntax - for varnamethatrepresentsasingleitem in list

#item represents each individual item as we loop through the list
for test_score in test_scores:
    print(test_score)

#modify items in a list to be read, however, this technique does not save the changes to the list
for test_score in test_scores:
    test_score = test_score + 5
    print(test_score)

print(test_scores)


# a list can also append (or add) things to it
#this means we can add additional data to a list when we need to 
#to do so we use the .append() method/function
new_score = 77
test_scores.append(new_score)
print(test_scores)

#now, what if we need to modify multiple items in our list at the same time, and those changes stick
#create a new list, and append the new data to the new list
#lets add 5 points to everyones test score
new_test_scores = []
for test_score in test_scores:
    test_score = test_score + 5
    new_test_scores.append(test_score)

# #overwrite the original, you can have it equal the new list you created
test_scores = new_test_scores
print(test_scores)

print(new_test_scores)

#python has really easy searching features in a list
#for instance, if I just want to see if something is in a list, I can use the in keyword to check..it will return a bool
looking_for = 100
found = looking_for in test_scores
print(found)

#I can search and remove..remove is done through the .remove() function/method
if found == True:
    print("Found the value")
    test_scores.remove(looking_for)
    print("Removed")
    print(test_scores)
else:
    print("Value not found")


