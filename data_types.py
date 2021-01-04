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
X = 'Hello World'                                    str
X = 20                                               int
X = 20.5                                             float
X = 1j                                               complex
X = ['apple', 'banana', 'cherry']                    list
X = ('apple', 'banana', 'cherry')                    tuple
X = range(6)                                         range
X = {'name': 'Adonis', 'age': 23}                    dict
X = {'apple', 'banana', 'cherry'}                    set
X = ({'apple', 'banana', 'cherry'})                  frozenset
X = True                                             bool
X = b'Hello'                                         bytes
X = bytearray(6)                                     bytearray
X = memoryview(bytes(6))                             memoryview


                                SETTING THE SPECIFIC DATA TYPES
If you want to specify the data type,you can use following constructor functions
Example                                                         DATA TYPE
X = str('Hello World')                                          str
X = int(20)                                                     int
X = float(20.5)                                                 float
X = complex(1j)                                                 complex
X = list(('apple', 'banana', 'cherry'))                         list
X = tuple(('apple', 'banana', 'cherry'))                        tuple
X = range(6)                                                    range
X = dict(name='Adonis', age=23)                                  dict
X = set(('apple', 'banana', 'cherry'))                           set
X = frozenset(('apple', 'banana', 'cherry'))                     frozenset
X = bool(5)                                                       bool
X = bytes(5)                                                      bytes
X = bytearray(5)                                                  bytearray
X = memorey(bytes(5))                                             memoryview
