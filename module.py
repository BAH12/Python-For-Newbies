                        PYTHON MODULES
What is a module?
consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application


                        CREATE A MODULE
To create a module just save the code you want in a file with the file extension .py
eg
Save this code in a file named mymodule.py

def greeting(name):
    print(f'Hello, {name}')


                            USE A MODULE
Now we can use the module we just created, by using the import statement
eg
Import the module named mymodule, and call the greeting function

import mymodule
mymodule.greeting('Adonis')

NOTE: When using a function from a module, use the syntax: module_name.function_name


                            VARIABLES IN MODULE
The module can contain functions, as already describe, but also, variables of all types (array, dictionary, object etc.)
eg
Save this code in the file mymodule

person1 = {
    'name': 'John',
    'age': 36,
    'country': 'Norway'
}

import the module named mymodule, and access the person1 dictionary

import mymodule
a = mymodule.person1['age']
print(a)


                                NAMING A MODULE
You can name the module file whatever you like, but it must have the file extension .py


                                RE - NAMING A MODULE
You can create an alias when you import a module by using the as keyword
eg
Create an alias for mymodule called mx

import mymodule as mx
a = mx.person1['age']
print(a)


                                BUILD-IN MODULES
There are severals built-in modules in python, which you can import whenever you like 
eg
Import and use the platform module

import platform
x = platform.system()
print(x)


                                USING THE dir() FUNCTION
There is a built-in function to list all the function names
(or variables names) in a module. The dir() function
eg
List all the defined names belonging to the platform module:
x = dir(platform)
print(x)

NOTE: The dir() function can be used on all modules, also the ones you create yourself


                                IMPORT FROM MODULE
You can choose to import only parts from a module, by using the from keyword
eg
The module name mymodule has one function and one dictionary
def greeting(name):
    print(f'Hello, {name}')

person1 = {  
    'name': 'John',
    'age': 36,
    'country': 'Norway'
}
eg
import only the person1 dictionary from the module

from mymodule import person1
print(person1['age'])

NOTE: When importing using the from keyword, do not use the module name when referring to elements in the module
eg
person1['age'], not mymodule.person1['age']
