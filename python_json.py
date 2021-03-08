                        PYTHON JSON
JSON is a syntax for storing and exchanging data

Json is text, written with Javascript Object Notation


                        JSON IN PYTHON
Python has a built-in package called json, which can be used to work with json Data
eg
import the json module
import json


                        PARSE JSON - CONVERT FROM JSON TO PYTHON
If you have a json string, you can parse it by using the json.loads() method
NOTE: The result will be a Python dictionary

eg
Convert from json to Python
x = '{"name": "John", "age": 30, "city": "Sierra Leone"}'
y = json.loads(x)
print(y)


                        CONVERT FROM PYTHON TO JSON
If you have a python object, you can convert it into a json string by using the json.dumps() method
eg
Convert from Python to json
x = {"name": "John", "age": 30, "city": "Sierra Leone"}
y = json.dumps(x)
print(y)


You can convert python objects of the following types, into json strings

dict
list
tuple
string
int
float
True
False
None

eg
Convert python objects into json strings, and print the value

import json

print(json.dumps({'name': 'John': 'age', 30, 'city': 'Sierra Leone'}))

print(json.dumps(['apple', 'banana', 'cherry']))


print(json.dumps(('apple', 'banana', 'cherry')))

print(json.dumps('Hello'))

print(json.dumps(42))

print(json.dumps(31.76))

print(json.dumps(True))

print(json.dumps(False))

print(json.dumps(None))


When you convert from python to json, Python objects are converted into the json (javascript equivalent) 

PYTHON                                      JSON

dict                                        object

list                                        array

tuple                                       array

str                                         string

int                                         number

float                                       number

True                                        true

False                                       false

None                                        null


Convert a python object containing all the legal data type 

import json

x = {
    'name': 'John',
    'age': 30,
    'married': True,
    'divorced': False,
    'children': ('Anna, Billy'),
    'pets': None,
    'cars': [
        {'model': 'BMW 230', 'mpg': '27.5'},
        {'model': 'Ford Edge', 'mpg': '24.1'}
        ]  
}
print(json.dumps(x))


                                FORMAT THE RESULT
The example above print a json string, but it is not very easy to read, with no indentations and line break

The json.dumps() method has parameters to make it easier to read the result
eg
Use the indent parameter to define the members of indent

x = {
    'name': 'John',
    'age': 30,
    'married': True,
    'divorced': False,
    'children': ('Anna, Billy'),
    'pets': None,
    'cars': [
        {'model': 'BMW 230', 'mpg': '27.5'},
        {'model': 'Ford Edge', 'mpg': '24.1'}
        ]  
}
print(json.dumps(x, indent=4))

You can also define the separators, default is (",", ":"), which means using a comma and a space to separate  each object, and a colon and a space to separate keys from values

print(x, indent=4, separators=(". ", " = "))


                            ORDER THE RESULT
The json.dumps() method has parameters to order the keys in the result
eg
Use the sort keys parameter to specify if the result should be sorted or not
print(json.dumps(x, indent=4, sort_keys=True))
