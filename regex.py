                        PYTHON REGEX
A Regex or Regular Expression, is a sequence of characters that forms a search pattern

Regex can be used to check if a string contains the specified search pattern.


                        REGEX MODULE
Python has a built-in package called 're' which can be used to work with regular expressions
import re


                        REGEX IN PYTHON
When you import the re module, you can start using regular expressions
eg
Search the string to see if it start with 'The' and ends with 'Spain'
import re
txt = 'The rain in Spain'
x = re.search('^The.*Spain', txt)
print(x)


                        REGEX FUNCTIONS
The re module offers a set of functions that allows us to search a string for a match

FUNCTION                DESCRIPTION

findall                 Returns a list containing all matches

search                  Returns a match object if there is a match
                        anywhere in the string

split                   returns a list where the string has been
                        split at each match 

sub                     Replaces one or many matches with a string


                        METACHARACTERS
Metacharacters are characters with special meaning

CHARACTER                   DESCRIPTION                         EXAMPLE

[]                          A set of characters                 '[a-m]'

\                           Signals a special sequence          '\d'
                            (can also be used to escape 
                            special characters)

.                           Any character                        'he..o'
                            (except newline character)

^                           Starts with                           '^hello'

$                           Ends with                             'world$'

*                           Zero or more occurrences              'aix*'

+                           One or more occurrences               'aix+'

{}                          Exactly the specified number          'al{2}'
                            of occurrences

|                           Either or                             'falls|stays'

()                          Capture and group


                            SPECIAL SEQUENCES
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning

CHARACTERS          DESCRIPTION                                 EXAMPLE

\A                  Returns a match if the specified            '\AThe'
                    characters are at the
                    beginning of the string

\b                  Returns a match where the specified         r'\bain'
                    characters are at the begining or at
                    the end of the word
                    (The 'r' in the begining is making sure     r'ain\b'
                    that the string is being treated as a 
                    'raw' string)

\B                  Returns a match where the specified         r'\Bain'
                    characters are present, BUT NOT at the
                    begining or at the end of the world         r'ain\B'

\d                  returns a match where the string
                    contain a digit(numbers from 0-9)           '\d'

\D                  Returns a match where the string
                    DOES NOT contain digits                     '\D'

\s                  Returns a match where the string            '\s'
                    contains whitespace character

\S                  Returns a match where the string            '\S'
                    DOES NOT containa whitespace characters 

\w                  Returns a match where the string contain     '\w'
                    any word(characters from A - Z, digits
                    from 0 - 9, and the underscore_ characters)

\W                  Returns a match where the string DOES NOT       '\W'
                    contain any word character

\Z                  Returns a match if the specified characters     '\Z'
                    are at the end of the string



                                    SETS
A set is a set of characters inside pair of square brackets [] with a spicial meaning

SET             DESCRIPTION

[arn]           Returns a match where one of the specified characters(a,r or n) are present

[a-n]           Returns a match for any lower case character alphabetically between a and n

[^arn]          Returns a match for any character EXCEPT a, r and n

[0123]          Returns a match where any of the specified digits(0, 1, 2, and 3) are present

[0-9]           Returns a match for any digits between 0 and 9

[0-5][0-9]      Returns a match for any two digits numbers from 00 and 59

[a-zA-Z]        Returns a match for any character alphabetically betwwn a and z lower or UPPER CASE

[+]             In sets +, *, ., |, (), $, {} has no special meaning, so [+] means: returns a match
                for any + character in the string



                                THE FINDALL() FUNCTION
The findall() function returns a list containing all matches
eg
print a list of all matches

import re
txt = 'The rain in Spain'
x = re.findall('ai', txt)
print(x)

The list contain the matches in the order they are found.
If no matches are found, an empty list is returned

eg
Return an empty list if no match was found

import re
txt = 'The rain in Spain'
x = re.findall('portugal', txt)
print(x)



                                THE SEARCH() FUNCTION
The search() function searches the string for a match, and returns a match object if there is a match

If there is more than one match, only the first occurrence of the match will be returned

eg
Search for the first whitspace character in the string

import re
txt = 'The rain in Spain'
x = re.findall('\s', txt)
print('The first whitspace character is located in the position:' x.start())

If no match are found, the value None is returned
eg
import re
txt = 'The rain in Spain'
x = re.findall('portugal', txt)
print(x)



                                    THE SPLIT() FUNCTION
The split() function returns a list where the string has been split at each match
eg
Split at each whitespace character

eg
import re
txt = 'The rain in Spain'
x = re.findall('\s', txt)
print(x)

You can control the number of occurrences by specifying the maxsplit parameter
eg
Split the string only at the first occurrences

eg
import re
txt = 'The rain in Spain'
x = re.findall('portugal', txt, 1)
print(x)



                                    THE SUB() FUNCTION
The sub() function replaces the matches with the text of your choice
eg
Replace every whitespace with the number 9

eg
import re
txt = 'The rain in Spain'
x = re.findall('\s', '9', txt)
print(x)

You can control the number of replacements by specifying the count parameter
eg
Replace the first 2 occurrences

import re
txt = 'The rain in Spain'
x = re.findall('\s', '9', txt, 2)
print(x)



                                        MATCH OBJECT
A match object is an object containing information about the search and the result

NOTE:If there is no match, the value None will be returned, instead of the match object
eg
Do a search that will return a match object

eg
import re
txt = 'The rain in Spain'
x = re.findall('ai', txt)
print(x)

The match object has properties and methods used to retrieve information about the search, and the result

SPAN() returns a tuple containing the start-, and the end position of the match

STRING() returns the string passed into the function

GROUP() returns the part ot the string where there was a match
eg
Print the position (start - amd  end position) of the first match occurrence

The regular expression looks for ant words that starts with an upper case 'S'


eg
import re
txt = 'The rain in Spain'
x = re.findall(r'\bS\w+', txt)
print(x.span())

eg
Print the part of the string where there was a match 
The Regular Expression looks for any words that starts with an uppers 'S'
eg
import re
txt = 'The rain in Spain'
x = re.findall(r'\bS\w+', txt)
print(x.group())

NOTE: If there is no match, the value None will be returned, instead of the match object
