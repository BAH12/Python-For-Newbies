                            PYTHON SCOPE
A variable is only from inside the region it is created.
This is called scope


                            LOCAL SCOPE
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function
eg
A variable created inside a function is available inside that function
def my_func():
    x = 'Local x'
    print(x)
my_func()


                            FUNCTION INSIDE FUNCTION
As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function
eg
The local variable can be accessed from a function within the function
def myfunc():
    x = 'local x'
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()


                            GLOBAL SCOPE
A variable created in the main body of the Python code is a global variable
belongs to the global Scope

Global variables are available from within any scope, global and local
eg
A variable created outside of a function is global and can be used by anyone
x = 'global x'
def myfunc():
    print(x)
myfunc()
print(x)


                            NAMING VARIABLES
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available  in the local scope
(inside the function)
eg
The function will print the local x, and then the code will print the global x:
x = 'global x'
def myfunc():
    x = 'local x'
    print(x)
myfunc()
print(x)


                            GLOBAL KEYWORD
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword

The global keyword makes the variable global 
eg
If you use the global keyword, the variable belongs to the global scope
def myfunc():
    global x
    x = 'global x'
myfunc()
print(x)

Also use the global keyword if you want to make a change to a global variable inside a function
eg
To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = 300
def myfunc():
    global x
    x = 200
myfunc()
print(x)