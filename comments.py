                                PYTHON COMMENTS
Comments can be used to explain python code
Comments can be used to make Python code more readable
Comments can be used to prevent code from executing when testing

                                CREATING A COMMENTS
Comments start with a '#' and python will ignore them
# This is a comment
print('Hello, Python Programmers')

Comments can be place at the end of a line and python will ignore the rest of the line
print('Hello, Python Programmers')# This is a comment

Comments does not have to be text to explain the code, it can also be used to prevent code from executing
# print('Hello, World')
print('Hello, Python Programmers')


                            MULTI LINE COMMENTS
Python does not really have a syntax for multiline comments
To add a multiline comment you could insert a '#' for each line
# This is a comment
# Written in
# More than just one line

Or, not quiet as intended you can use a multiline string 
since python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code and place you comments inside it
"""
This is a comment 
Written in 
More than just one line
"""

As long the string is not assigned to a variable python will read the code, but then ignore it, and you have made a multiline comment