                            BOOLEANS
Booleans represent one or two values: True or False

                            BOOLEAN VALUE
In programming you often need to know if an expression is True or False
You can evalute any expression in python,and get one or two answers, True or False
When you compare two values the expression is evaluted and Python returns the Boolean Answer
eg
print(10 > 9)
print(10 == 9)
print(10 < 9)

When you run a condition in an if statement,Python returns True or False

Print a message based on whether is True or False
x = 200
y = 33
if x > y:
    print('x is greater than y')
else:
    print('y is not greater than x')

                            EVALUTE VALUES AND VARIABLES
The bool() function allows you to evalute any value and give you True or False
eg
Evalute a string and a number
print(bool('Hello'))
print(bool(15))

Evalute two variables
x = 'Hello'
y = 15
print(bool(x))
print(bool(y))

                            MOST VALUES ARE TRUE
Almost any value is evaluted to True if it has some sort of content
Any string is True except empty 0
Any list,tuple,set and dictionary are True,except empty ones
eg
The following will return True
print(bool('abc'))
print(bool(123))
print(bool(['apple', 'banana', 'cherry']))

                            SOME VALUES ARE FALSE
In fact not many values that evalute to False
except empty values such as (), [], {}, " " the number 0, and the value None
And of course the value False evalute to False
eg
The following will return False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(' '))
print(bool(()))
print(bool([]))
print(bool({}))

One more value or object in this case,evalutes to false, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

                        FUNCTIONS CAN RETURN A BOOLEAN
You can create a function that returns a Boolean value
eg
print the answer of a function
def myfunc():
    return True
print(myfunc())

You can execute code based on the Boolean answer of a function
eg
print 'YES' if the function returns True otherwise print 'NO'

def my_function():
    return True
if my_function():
    print('YES')
else:
    print('NO')

Python has many built-in functions that returns a boolean value, like the isistance()function, which can be used to determine if an object is of a certain data Type
eg
Check if an object is an integer or not:
x = 200
print(isistance(x, int))
