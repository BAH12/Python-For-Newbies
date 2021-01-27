                            PYTHON TUPLE
Tuples are used to store multiple items in one variable
Tuple is one of the 4 built-in data types in python used to store collection of data, the other three  are LIST, SET, and DICTIONARY all with different qualities and usage

Tuple is a collection which is ordered and unchangeable
Tuples are written with round brackets ()
fruits = ('apple', 'banana', 'cherry')
print(fruits)



                            TUPLE ITEMS
Tuple items are ordered, unchangeable and allow duplicate values
Tuples items are indexed, the first item has index [0], the second has index [1]



                            ORDERED
When we say tuples are ordered, it means that the items have a define order, and that order will not change



                            UNCHANGEABLE
Tuples are unchangeable, means that we cannot change, add or remove items after the tuple has been created



                            ALLOW DUPLICATES
Since tuples are indexed, tuples can have items with the same name 
eg
fruits = ('apple', 'banana', 'cherry', 'apple', 'banana')
print(fruits)



                            TUPLE LENGTH
To determine how many items the tuple has, use the len() function 
fruits = ('apple', 'banana', 'cherry')
print(len(fruits))



                            CREATE TUPLE WITH ONE ITEM
To create a tuple with one item, you have to add a comma after the item, otherwise python will not recognise it as a tuple
x = ('Bah',)



                            TUPLE ITEMS - DATA TYPES
Tuple items can be any data type
tuple1 = ('apple', 'banana', 'cherry')
tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple3 = (True, False, True)
print(tuple1)
print(tuple2)
print(tuple3)

A tuple can contain different data types
tuple1 = ('abc', 34, True, 35.8, 'male')



                                TYPE()
From Python perspective, tuples are defined as object with the data type 'tuple'
tuple1 = ('apple', 'banana', 'cherry')
print(type(tuple1))



                                THE TUPLE () CONSTRUCTOR
It is also possible to use the tuple constructor to make a tuple
mytuple = tuple(('apple', 'banana', 'cherry'))
print(mytuple)



                                PYTHON - ACCESS TUPLE ITEMS
ACCESS TUPLE ITEMS
You can access tuple items by referring to their index number, inside square brackets
fruits = ('apple', 'banana', 'cherry')
print(fruits[0])
NOTE: The first item has index 0



                                NEGATIVE INDEXING
Negative indexing means starting from the end
-1 refers to the last item -2 refers to the second to last item etc



                                RANGE OF INDEXES
You can specify a range of indexes by specifying where to start and where to end the range
When specifying a range, the return value will be a new tuple with the specified items
fruits = ('apple', 'banana', 'cherry', 'melon', 'orange', 'kiwi', 'pineapple')
print(fruits[2:5])
NOTE: The search will start at index 2 (included) and end at 5 (not included)
By leaving out the start value, the range will start at the first item and also do the same if you leave out the end index
fruits = ('apple', 'banana', 'cherry', 'melon', 'orange', 'kiwi', 'pineapple')
print(fruits[:5])

fruits = ('apple', 'banana', 'cherry', 'melon', 'orange', 'kiwi', 'pineapple')
print(fruits[2:])



                                RANGE OF NEGATIVE INDEXES
Specifying negative indexes if you want to start the search from the end of the tuple
eg
This returns the items from index -4 (included) to index -1 (not included)
fruits = ('apple', 'banana', 'cherry', 'melon', 'orange', 'kiwi', 'pineapple')
print(fruits[-4:-1])



                                CHECK IF ITEMS EXISTS
To determine if a specified item is present in a tuple use the 'in' keyword
fruits = ('apple', 'banana', 'cherry')
if 'apple' in fruits:
    print('Yes it is present')




                                PYTHON - UPDATE TUPLE
Tuples are unchangeable, meaning that you cannot change, add, and remove an items once the tuple is created
But there is workaround

                                CHANGE TUPLE VALUES
Once a tuple is created, you cannot change it values UNCHANGEABLE or IMMUTABLE as it also is called
But there is a workaround.
You can convert the tuple into a list, change the list and convert the list back to tuple
eg
fruits = ('apple', 'banana', 'cherry')
x = list(fruits)
x[2] = 'kiwi'
fruits = tuple(x)
print(fruits)



                                ADD ITEM
Once a tuple is created you cannot add item to it 
Just like the workaround for changing a tuple, you can convert it into a list, add your items and convert it back to a tuple
eg
Convert the tuple into a list, add 'orange' and convert it back into a tuple
fruits = ('apple', 'banana', 'cherry')
x = list(fruits)
x.append('orange')
fruits = tuple(x)
print(fruits)



                            REMOVE ITEMS
NOTE: You cannot remove items in a tuple 
Tuples are UNCHANGEABLE, so you cannot remove items from the tuple
But you van use the same workaround as we used for changing and adding tuple item
fruits = ('apple', 'banana', 'cherry')
x = list(fruits)
x.remove('cherry')
fruits = tuple(x)
print(fruits)

Or you can delete the tuple completely 
The 'del' keyword deletes the tuple completely
fruits = ('apple', 'banana', 'cherry')
del fruits
print(fruits)



                            PYTHON - UNPACKING TUPLES
UNPACKING A TUPLE
When we create a tuple, we normally assign values to it
This is called 'packing' a tuple
fruits = ('apple', 'banana', 'cherry')

But in python, we are also allowed to extract the values back into variables
This is called unpacking 
fruits = ('apple', 'banana', 'cherry')
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

NOTE: The number of variables must match the number of values in the tuple, if not, you must use an asterix * to collect the remaining values as a list
fruits = ('apple', 'banana', 'cherry')
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


                            USING ASTERIX *
If the number of variable is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'pineapple')
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

If the asterix is added to another variable name than the last, Python will assign values to the variable until the number of values left matched
fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'pineapple')
(green, *tropical, red) = fruits
print(green)
print(tropical)
print(red)



                            PYTHON LOOP TUPLES
You can loop through the tuple items by using a 'for' loop 
fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'pineapple')
for x in fruits:
    print(x)



                            LOOP THROUGH THE INDEX NUMBERS
You can also loop through the tuple items by referring to their index
Use the range() and len() functions to create a suitable iterable
fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'pineapple')
for x in range(len(fruits)):
    print(fruits[x])


                            USING A WHILE LOOP
You can loop through the tuple items by using a while loop
Use the len() function to determine the length of the tuple, by referring to their indexes
Remember to increase the index by 1 after each iteration
fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'pineapple')
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1



                            PYTHON - JOIN TUPLES
JOIN TWO TUPLES
To join two or more tuples, you can use the + operator
x = ('a', 'b', 'c')
y = (1, 2, 3, 4, 5)
z = x + y
print(z)


                            MULTIPLY TUPLE
If you want to multiply the content of a tuple a given number of times, you can use the * operator
fruits = ('apple', 'banana', 'cherry')
x = fruits * 2
print(fruits)



                            PYTHON TUPLE METHODS
Python has two built-in methods that you can use on tuple

METHOD                      DESCRIPTION
count()                     Returns the number of times a specified value occurs
                            in a tuple

index()                     Searches the tuple for a specified value and returns
                            the position of where it was found