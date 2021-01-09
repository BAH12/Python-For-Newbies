                                PYTHON STRINGS

Strings in python are surrounded by quotation marks,
or double quotation marks
'hello' is the same as "hello"
You can display string literal with the print() function
eg
print('Hello')
print("Hello")


                            ASSIGN STRING TO A VARIABLE
Assigning a string to a variable is done with the variable name followed by an equal sign and the string.
eg
a = 'hello'
print(a)


                                MULTILINE STRINGS
You can assign a multiline string to a variable by using three quotes
eg
a = """
This is a 
multiline string
"""
is the same as
a = '''
This is a 
multiline string
'''
NOTE: In the result,the line breaks are inserted at the same position


                            STRINGS ARE ARRAYS
Like any other Programming Language,strings in python are Arrays of bytes representing unicode characters

However, Python does not have a character data type, a single character is simply a string with a length of 1

Square brackets can be used to access elements of the string

eg
Get the character at position 1 (remember that the first character has the position 0)
a = 'Hello World'
print(a[1])


                                LOOPING THROUGH A STRING
Since strings are arrays, we can loop through the characters in a string with a for loop
eg
Loop through the letters in the word 'banana'
for x in 'banana':
    print(x)


                                STRING LENGTH
To get the length of a string, use the len() function
eg
The len() function returns the length of a string
a = 'Hello World'
print(len(a))


                                CHECK STRING
To check if a certain phrase or character is present in a string, we can use the keyword in..
eg
Check if 'free' is present in the following text
txt = 'The best things in life are free'
print('free' in txt)

Use the if statement
print only if 'free' is present
txt = 'The best things in life are free'
if 'free' in txt:
    print('Yes, is present')

                                CHECK IF NOT
To check if a certain phrase or character is NOT present in string, we can use the keyword 'not' in 
eg
Check if 'expensive' is NOT present in the following text
txt = 'The best things in life are free'
print('expensive' not in txt)

use it in an if statement
print only 'if' 'expensive' is NOT present
txt = 'The best things in life are free'
if 'expensive' not in txt:
    print('Yes, Expensive is NOT present')


                                PYTHON SLICING STRINGS
Slicing, You can return a range of characters by using the slice syntax
Specify the start index and the end index, separeted by colon : to return a part of the string 
eg
Get the characters from position 2 to position 5 (not included)
a = 'Hello World'
print(b[2:5])
NOTE: The first character has index 0


                SLICE FROM THE START
By leaving out the start index, the range will stat at the first character
eg
Get the characters from the start to the  position 5(but not included)
a = 'Hello World'
print(a[:5])

                SLICE TO THE END
By leaving out the end index, the range will go to the end
Get the characters from position 2, and all the way to the end
b = 'hello world'
print(2:)

                NEGATIVE INDEXING 
Use the negative indexes to start the slice from the end of the string
eg
Get the characters:
From 0 in the 'World' (position -5)
To, but not included: 'd' in the 'World'(position -2)
c = 'Hello World'
print(c[-5:-2])

                        MODIFY STRINGS
Python has a set of built-in methods that you can use on strings

                        UPPER CASE
The upper() method returns the string in upper case
a = 'hello world'
print(a.upper())

                        LOWER CASE
The lower() method returns the string in lower case
a = 'hello world'
print(a.lower())

                        REMOVE WHITESPACE
The strip() method remove any whitespaces from the beginning or the end 
a = 'hello world'
print(a.strip())

                        REPLACE STRING
The replace() method replaces a string with another string
a = 'Hello World'
print(a.replace('H', 'B'))

                        SPLIT STRING
The split() method splits the string into substrings if it finds instances of the separator
a = 'helloworld'
print(a.split(','))

                        STRING CONCATENATION
To concatenation or combine two strings you can use the + operator
a = 'hello'
b = 'world'
c = a + b
print(c)


                            FORMAT STRING
As we learned in Python variables chapter, we can not combine strings and numbers like this
age = 43
txt = 'My name is John, I am + 'age

But we can combine strings and numbers using the format() method
The format methods takes the passes argument formats them and places them in the where the placeholder {} are
Use the format() method to insert numbers into strings 
age = 43
txt = 'My name is John, I am {}'
print(txt.format(age)) 

The format() method takes unlimited number of arguments and are place into the the respective placeholders
quantity = 3
itemnum = 567
price = 49.95
my_order = 'I want {} pieces of item {} for {} dollars'
print(my_order.format(quantity, itemnum, price))

You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemnum = 567
price = 49.95
my_order = 'I want {2} pieces of item {0} for {1} dollars'


                                ESCAPE CHARACTERS
To insert characters that are legal in a string use an escape character...
An escape character is a backslash / followed by the character you want to insert
An illegal character is a double quote inside a string that is surrounded by double quotes

You will get an error if you use double quotes inside a string that is surrounded by double quotes
txt = " We are the so-called "vikings" from the north"
To fix this problem, use the escape character /
txt = 'We are the so-called "vikings" from the north'

The escape character allows you to use double quotes when you normally would not be allowed

Other Escape characters used in Python 

CODE                                        RESULT
\'                                          Single Quote
\\                                          Backslash
\n                                          New Line
\r                                          Carriage Return
\t                                          Tab
\b                                          Backspace
\f                                          Form Feed
\000                                        Octal Value
\xhh                                        Hex Value


                                STRING METHODS
Python has a built-in methods that you can use on strings 
NOTE: All string methods returns new values.They do not change the original string

METHOD                      DESCRIPTION
capitalize()                Convert the first character to upper case

casefold()                  Converts string into lower case

center()                    Returns a centered string

count()                     Returns the number of times a specific value occur in
                            a string

encode()                    Returns an encode version of the string

endswith()                  Retruns True if the string end with the specific value

expandtabs()                Sets the size of the string

find()                      Searches the string for a specified value and return
                            the position of where it was

format()                    Formats specified values in a string

format_map()                Formats specified values in a string

index()                     Searches the string for a specified value and
                            returns the position of where it was found

isalnum()                   Retruns True if all characters are alphanumeric

isdecimal()                 Returns True if all characters in the string are decimals

isdigit()                   Returns True if all characters in the string are digits

isidentifier()              Returns True if the string an identifier 

islower()                   Returns True if all character in the string are
                            lower case

isnumeric()                 Returns True if all characters in the string are numeric

isprintable()               Returns True if all characters in the string is printable

isspace()                   Returns True if all characters in the string are
                            whitespaces

istitle()                   Returns True if the string followed the rule of a title

isupper()                   Returns True if all characters in the string are
                            upper case

join()                      Joins the elements of an iterable to the end
                            of the string

ljust()                     Returns left justified version of the string

lower()                     Converts a string into lower case

lstrip()                    Returns a left trim version of the string

maketrans()                 Retruns a translation table to used in translations

partition()                 Returns a tuple where the string is parted
                            into three parts

replace()                   Retruns a string where a specified value
                            is replaced with a specified value

rfind()                     Searches the string for a specified value and returns
                            the last position of where it was found

rindex()                    Searches the string for a specified
                            value and returns the last position of where it was found

rjust()                     Returns a right justified version of the  string  

rpartition()                Returns a tuple where the string is parted into three
                            parted

rsplit()                    Splits the string at the specified separator and
                            returns a list

rstrip()                    Returns a right trim version of the string

split()                     Splits the string at the specified separators, and
                            returns a list

splitlines()                Splits the string at line breaks and returns a list

startwith()                 Returns True if the string starts with the
                            specified value

strip()                     Returns a trimmed version of the string

swapcase()                  Swap cases, lower case becomes upper case vice versa

title()                     Converts the first character of each word to upper case

translate()                 Returns s translated string

upper()                     Converts a string to upper case

zfill()                     Fills the string with a specified number of values of
                            the beginning