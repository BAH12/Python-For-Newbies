                        PYTHON IF...ELSE..
PYTHON CONDITIONS AND IF STATEMENT
Python support the usual logical conditions from mathematics

equal: a == b
not equal to: a != b
less than: a < b
less than or equal to: a <= b
greater than: a > b
greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in 'if' statement and loops
An if statement is written by using the 'if' keyword
eg
a = 33
b = 200
if b > a:
    print('b is greater than a')
In the example above we use two variables, a and b, which are used as part of the if statement to test wheather b is greater than a. As a is 33 and b is 200, we know that 200 is greater than 33, and so we print to screen that 'b is greater than a'


                                    INDENTATION
Python relies on indentation (whitespace at the beggining of a line of code)
Other Programming Languages use curly brackets for this purpose
eg
if statement, without indentation will raise an error
a = 33
b = 200
if b > a:
print('b is greater than a') # You will get an error


                                    ELIF
The 'elif' keyword is pythons way of saying if the previous condition was not True
then try this condition
a = 33
b = 33
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')
In this example a is equal to b, so the first condition is not True, but the elif condition is True, so we print to screen that 'a and b are equal'


                                ELSE
The else keyword catches anything which is not caught by the preceding conditions
a = 200
b = 33
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')
else:
    print('a is greater than b')


                                SHORT HAND IF
If you have only one statement to execute, you can put it on the same line as the if statement
a = 200
b = 33
if a > b: print('a is greater than b')


                                SHORT HAND IF...ELSE
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
a = 22
b = 330
print('A') if a > b else print('B')


                                AND
The 'and' keyword is a logical operator, and it us used to combine condition statements
eg
Test if a is greater than b, and if c is greater than a
a = 200
b = 33
c = 500
if a > b and c > a:
    print('Both conditions are True')


                                    OR
The 'or' keyword is a logical operator, and is used to combine conditional statements
eg
Test if a is greater than b, or a is greater than c
a = 200
b = 33
c = 500
if a > b or a > c:
    print('At least one of the conditions is True')


                                NESTED IF
You can have if statement inside if statement, this is called nested if statement
x = 41
if x > 10:
    print('Above ten')
    if x > 20:
        print('And also above 20!')
    else:
        print('But not above 20')


                                THE PASS STATEMENT
If statement cannot be empty, but if you for some reason have an if statement with no content, put in the 'pass' statement to avoid getting an error
a = 33
b = 200
if b > a:
    pass 