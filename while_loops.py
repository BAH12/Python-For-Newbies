                                PYTHON WHILE LOOPS
                                
Python has two primitive loop commands
while loop
for loop

With the 'while' loop we can execute a set of statement as long as a condition is true
eg
print i as long as i is less than 6
i = 1
while i < 6:
    print(i)
    i += 1

NOTE: Remember to increment i, or else the loop will continue forever

The 'while' requires a relevant variables to be ready, in this example we need to define an indexing variable i, which we set to 1


                            THE BREAK STATEMENT
With the 'break' statement we can stop the loop even if the while condition is true
eg
Exit the loop when i is 3
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


                            THE CONTINUE STATEMENT
With the 'continue' statement we can stop the current iteration, and continue with the next:
eg
Continue to the next iteration if i is 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


                            THE ELSE STATEMENT
With the 'else' statement we can run a block of code once the condition no longer is true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')