                        PYTHON DATA TYPES
BUILD-IN DATA TYPES
In programming data types is an important concept.
Variables can store data of different data types and different types can do different things

Python has the following data types built-in by default in these categories

Text type : str
Numeric type : int,float,complex
Sequence type : list,tuple,range
Mapping type: dict
Set type: set, frozenset
Boolean type: bool
Binary type: bytes,bytearray,memoryview

                    GETTING THE DATA TYPE
You can get the data type of any object by using the type () function
x = 5
print(type(x))


                            SETTING THE DATA TYPE
In programming,the data type is set when you assign a value to the variable:
Example                                              DATA TYPE
x = 'Hello World'                                    str
x = 20                                               int
x = 20.5                                             float
x = 1j                                               complex
x = ['apple', 'banana', 'cherry']                    list
x = ('apple', 'banana', 'cherry')                    tuple
x = range(6)                                         range
x = {'name': 'Adonis', 'age': 23}                    dict
x = {'apple', 'banana', 'cherry'}                    set
x = ({'apple', 'banana', 'cherry'})                  frozenset
x = True                                             bool
x = b'Hello'                                         bytes
x = bytearray(6)                                     bytearray
x = memoryview(bytes(6))                             memoryview


                                SETTING THE SPECIFIC DATA TYPES
If you want to specify the data type,you can use following constructor functions
Example                                                         DATA TYPE
x = str('Hello World')                                          str
x = int(20)                                                     int
x = float(20.5)                                                 float
x = complex(1j)                                                 complex
x = list(('apple', 'banana', 'cherry'))                         list
x = tuple(('apple', 'banana', 'cherry'))                        tuple
x = range(6)                                                    range
x = dict(name='Adonis', age=23)                                  dict
x = set(('apple', 'banana', 'cherry'))                           set
x = frozenset(('apple', 'banana', 'cherry'))                     frozenset
x = bool(5)                                                       bool
x = bytes(5)                                                      bytes
x = bytearray(5)                                                  bytearray
x = memorey(bytes(5))                                             memoryview
