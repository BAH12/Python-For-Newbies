                            PYTHON VARIABLES
Variables are containers for storing data values

                        CREATING VARIABLES
Python has no command for declaring a variable
A variable is created the moment you first assign a value to it
x = 5
y = 'John'
print(x)
print(y)

Variables do not need to be declared with any particular type and can even change type after they have been set
x = 4 # x is the type integer
x = 'John' # x is the type string

                                CASTING
If you want to specify the data type of a variable this can be done with casting
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0


                                GET THE TYPE
You can get the data type of a variable with the type() function
x = 5
y = 'John'
print(type(x))
print(type(y))


                                SINGLE OR DOUBLE QUOTE
String variables can be declared either by using single or double quotes
x = 'john'
# is the same as
x = "john"


                                CASE-SENSITIVE
Variable names are case-sensitive 
a = 4
A = 'john'
# A will not overwrite a


                                VARIABLE NAMES
A variable can have a short name like ( x and y) or more descriptive names like(age, carname, total_volume)


                        RULES FOR PYTHON VARIABLES
A variable name must start with a letter or the underscore character
A variable name cannot start with a number 
A variable name can only contain Alpha-Numeric characters and the underscore( A - Z and 0 - 9 and the underscore _)
Variable names are case-sensitive(age and Age are different variable)

Legal variable names:                   
myvar = 'john'
my_var = 'john'
_my_var = 'john'
myVar = 'john'
MYVAR = 'john'
myvar2 = 'john'

Illegal variable names:
2myvar = 'john'
my-var = 'john'
my var = 'john'

note = REMEMBER THAT VARIABLES NAMES ARE CASE-SENSITIVE

Variables names with more than one word can be difficult to read
There are several techniques you can use to make them more readable

CAMEL-CASE = Each word,execept the first,start with a capital letter
myVariableName = 'john'

PASCAL-CASE = Each word start with a capital letter
MyVariableName = 'john'

SNAKE-CASE = Each word is seperated with the underscore character
my_variable_name = 'john'


                            ASSIGN MULTIPLE VALUES
Many values to multiple variables
Python allows you to assign values to multiple variables in one line
x, y, z = 'apple','banana','cherry'

note: Make sure the number of variable matches the number of values,or else you will get an error

                        ONE VALUES TO MULTIPLE VARIABLES
And you can assign the same values to multiple variable in one line
x = y = z = 'orange'


                            UNPACKING A COLLECTION
If you have a collection of values in a list,tuple etc .
Python allows you to extract the values into variables
This is called unpacking
fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits


                                OUTPUT VARIABLES
The python print() statement is often used to output variables 
To combine both text and variable,python uses the plus + character
x = 'awesome'
print('Python is '+ x)

You can also use the plus + character to add a variable to another variable
x = 'python is '
y = 'awesome'
z = x + y
print(z)

For numbers,the plus + character works as a mathematical operator
x = 5
y = 10
print(x + y)

note: If you try to combine a string and a number,Python will give you an error
x = 5
y = 'john'
print(x + y)


                                GLOBAL VARIABLES
Variables that created outside of a function (as in all of the example above)are known as global variables 
Global variables can be used by everyone both inside of a function and outside

example
Create a variable outside of a function and use it inside the function
x = 'awesome'
def myfunc():
    print('Python is ' + x)

myfunc()

If you create a variable with the same name inside a function this variable will be local,and can only be used inside a function.
The global variable with same name will remain as it was,global and with the original value

Create a variable inside a function with the same name as the global variable
x = 'awesome'
def myfunc():
    x = 'fantastic'
    print('Python is '+ x)

myfunc()
print('Python is ' + x)


                                THE GLOBAL KEYWORD
Normally you can create a variable inside a function, that variable is local and can only be used inside that function

To create a global variable inside a function you can use the global keyword
example
If you use the global keyword the variable belongs to the scope
def myfunc():
    global x
    x = 'fantastic'


myfunc()
print('Python is '+ x)

Also use the global keyword if you want to change a global inside a function
example
To change the value of a global variable inside a function refer to the variable by using the global keyword
x = 'awesome'
def myfunc():
    global x
    x = 'fantastic'

myfunc()
print('Python is ' +x)
