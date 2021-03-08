                            PYTHON TRY EXCEPT
The try block lets you test a block of code for errors 
The except block lets you handle the error
The finally block lets you execute code, regardless of the result of the try and except
block


                            
                            EXCEPTION HANDLING
When an error occurs, or exception as we called it, python will normally
stop and generate an error message
These exceptions can be handled using the try statement
eg
The try block will generate an Exception, because x is not define
try:
    print(x)
except:
    print('An exception occured')

Since the try block raise an error, the Exception block will be executed
eg
print(x) 


                            MANY EXCEPTIONS 
You can define as many Exception blocks as you want 
eg
If you want to execute a special block of code for a special kind of error
eg
Print one message if the try block raises a 'NameError' and another for other error

try:
    print(x)
except NameError:
    print('Variable x is not define')
except:
    print('Somthing else went wrong')



                                    ELSE
You can use the else keyword to define a block of code to be executed
if no errors were raised
eg
In this example, try block does not generate an error
try:
    print('Hello')
except:
    print('Somethin went wrong')
else:
    print('Nothing went wrong')


                                FINALLY
The finally block, if specified will be executed regarding if the try block
raises an error or not 
eg
try:
    print(x)
except:
    print('Somethin went wrong')
finally:
    print('Executing the finally block')

This can be useful to close objects and clean up resourses
eg
Try to open and write a file that is not writable
try:
    f = open('demo.txt')
    f.write('Lorem Ipsum')
except:
    print('Somethin went wrong when writting to the file')
finally:
    f.closd()

The program can continue without leaving the file object open


                            RASISE AN EXCEPTION
As a python developer you can choose to throw an exception if a condition occurs
To throw or to raise an exeception, use the raise keyword
eg
Raise an error and stop the program if x is lower than 0
x = -1
if x < 0:
    raise Exception('Sorry, no number below zero')

The raise keyword is used to raise an exception 
You can define what kind of error to raise, and the text to print to the user
eg
Raise a TypeError if x is not an integer
x = 'hello'
if not type(x) is int:
    raise TypeError('Only integers are allowed')