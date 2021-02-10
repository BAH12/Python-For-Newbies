                            PYTHON FUNCTION
A function is a block of code which only runs when it is called
You can pass data, known as parameter, into a function
A function can return data as a result


                            CREATING A FUNCTION
In python a function is defined using the def keyword
def my_func():
    print('Hello from a Function')


                            CALLING A FUNCTION
To call a function, use the function name followed by parenthesis
def my_func():
    print('Hello from a Function')
my_func()


                            ARGUMENT
Information can be passed into a function as argument
Arguments are specified after the function name, inside the parenthesis
You can add as many arguments you want, just separate them with comma

The following example has a function with one argument( first_name ).
When the function is called, we pass along with first name, which is used inside the function to print the full name
def my_family(first_name):
    print(f'{first_name} Refsnes')
my_family('Emil')
my_family('Tobias')
my_family('Linus')
NOTE: Argument are often shortened to args in Python documentation


                                PARAMETER or ARGUMENT
The terms Parameter and Argument can be used for the same thing:
Information that are passed into a function
NOTE: From Python perspective: A Parameter is a variable listed inside the parenthesis in the function definition
An Argument is the value that is sent to the function when it is called


                                NUMBER OF ARGUMENT
By default, a function must be called with the correct number of argument.Meaning if your function expects two 2 arguments, you have to call the function with 2 arguments, not more, and not less
eg
This function expects 2 arguments, and get 2 arguments
def my_func(first_name, last_name):
    print(f'{first_name} {last_name}')
my_func('Emil', 'Refsnes')
NOTE: If you try to call the function with 1 or 3
arguments, you will get an error


                            ARBITRARY ARGUMENTS, args
If you do not know how many arguments that will be passed into the function, add an asterisk * before the parameter name in the function definition
This way the function will receive a tuple of arguments, and access the items accordingly
eg
If the number of arguments is unknown, add an asterisk * before the parameter names
def my_family(*kid):
    print(f'The youngest child is {kid[2]}')
my_family('Emil', 'Tobias', 'Linus')
NOTE: Arbitrary arguments are often shortend to *args in Python documentation


                            KEYWORD ARGUMENT
You can also send arguments with key = value syntax
This way the order of the arguments doesnot matter
def my_family(child1, child2, child3):
    print(f'The youngest child is {child3}')
my_family(child1='Emil', child2='Tobias', child3='Linus')
NOTE: The phrase keyword arguments are often shortened to kwargs in Python documentation


                            ARBITRARY KEYWORD ARGUMENTS, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two (2) asterisk ** before the parameter name in the function definition
This way the function will receive a dictionary of arguments, and access the items accordingly
eg
If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_family(**kid):
    print(f'His last name is {kid["last_name"]}')
my_family(first_name='Tobias', last_name='Refsnes')
NOTE: Arbitrary keyword arguments are often shortened  to **kwargs in Python documentation


                                DEFAULT PARAMETER
The following examples show how to use a default parameter value:
If we call the function without argument, it uses the default value
def my_country(country='Sierra Leone'):
    print(f'I am from {country}')
my_country('Sweden')
my_country('India')
my_country()
my_country('Brazil')


                                PASSING A LIST AS AN ARGUMENT
You can send any data types as argument to a function(string, list, tuple, etc.), and will be treated as the same data type inside function
eg
If you send a list as an argument, it will still be a list when it reaches the function
def foodlist(food):
    for x in food:
        print(x)
fruits = ['apple', 'banana', 'cherry']
foodlist(fruits)


                                    RETURN VALUES
To let a function, return a value, use the return statement
def my_func(x):
    return 5 * x
print(my_func(3))
print(my_func(5))
print(my_func(9))


                                    THE PASS STATEMENT
Function definition cannot be empty, but if you for some reason have a function definition with no content, put in the 'pass' statement to avoid getting an error
def myfunc():
    pass


                                    RECURSION
Python also accepts function recursion, which means a defined function can call itself

Recursion is a common mathematical and programming concept...It means that a function call itself...
This has the benefits of meaning that you can loop through to reach a result...

The developer should be very careful with recursion as it can be easily to slip into writing a function which will never terminate, or that uses processor power.
However, when written correct recursion can be very efficient and mathematically-elegant approach to programming

In this examples, tri_recursion() is a function that we have defined to call itself ( 'recursion' ). We use the K variable as data, which decrement ( -1 ) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0)
To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print('\n\n Recursion Example Results')
tri_recursion(6)