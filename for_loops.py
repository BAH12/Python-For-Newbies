                        PYTHON FOR LOOPS

A 'for' loop is used to iterate over a sequence ( that is either a list, a tuple, a set, a dictionary or a string )

This is less like the 'for' keyword in other Programming Languages, and works more like an iterator method as found in other object-oriented-Programming Languages

With the 'for' loop we can execute a set of statements, once for each item in a list, set etc
eg
Print each fruit in a fruit list
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

The for loop doesnot require an indexing variable to set beforehand


                            LOOP THROUGH A STRING
Even strings are iterable objects, they contain a sequence of characters
eg
Loop through the letters in the word 'banana'
for x in 'banana':
    print(x)


                                THE BREAK STATEMENT
With the break statement we can stop the loop before it has looped through all the items
eg
Exit the loop when x is 'banana'
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

Exit the loop when x is 'banana' but this time the break comes before the print
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        break
    print(x)


                                THE CONTINUE STATEMENT
With the continue statement we can stop the current iteration of the loop, and continue with the next
eg
Do not print 'banana'
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)


                                THE RANGE() FUNCTION
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers starting from 0 by default, and increment by 1 ( by default ), and ends at a specified number
eg
Using the range() function
for x in range(6):
    print(x)

NOTE: Note that the range() function default to 0 as a starting value, however, it is possible to specify the starting value by adding a parameter
range(2, 6), which means values from 2 to 6 ( but not included )
eg
Using the start parameter
for x in range(2, 6):
    print(x)

The range() function default to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter
range(2, 30, 3)
eg
Increment the sequence with 3 ( default is 1 )
for x in range(2, 30,3):
    print(x)


                            THE ELSE IN FOR LOOP
The 'else' keyword in a for loop specifies a block of code to be execute when is finished
eg
print all numbers from 0 to 5, and print a message when the loop finished
for x in range(6):
    print(x)
else:
    print('Finally finished')

NOTE: The 'else' block will NOT be executed if the loop is stopped by a break statement
eg
Break the loop when x is 3, and see what happens with the else block
for x in range(6):
    if x == 3:
        break
else:
    print('Finally finished')***


                            NESTED LOOPS
A nested loop is a loop inside a loop.
The inner loop will be executed one time for each iteration of the outer loop
eg
print each adjective for every fruit:
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)


                            THE PASS STATEMENT
for loop cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error
for x in [0, 1, 2, 3, 4, 5]:
    pass