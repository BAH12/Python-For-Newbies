                    PYTHON CLASSES AND OBJECTS
Python is an object-oriented Programming language
Almost everything in Python is an object, with its properties and methods
A class is like a object constructor, or a blueprint for creating object


                    CREATE A CLASS
Create a class named my_class, with a property named x
class my_class:
    x = 5
print(my_class)


                    CREATE AN OBJECT
Now we can use the class my_class to create an object:
eg
create an object name p1, and print the value of x
class my_class:
    x = 5
p1 = my_class()
print(p1.x)


                    THE __INIT__() FUNCTION
The examples above are classes and objects in their simplest form, and are not really useful in real life

To understand the meaning of classes we have to understand
the built-in __init__(), which is  always executed when the class is being initiated

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

eg
create a class name Person, use the __init__() function to assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Abubakarr Bah', 23)
print(p1.name)
print(p1.age)
NOTE:The __init__() function is called automatically every time the class is being used to create a new object


                        OBJECT METHODS
Objects can also contain methods. Methods in objects are functions that belong to the object

Let us create a method in the Person class
eg
Insert a function that print a greeting, and execute it on the p1 object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def my_func(self):
        print('Hello my name is ' + self.name)
p1 = Person('Abubakarr Bah', 23)
p1.my_func()
NOTE:The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class


                        THE SELF PARAMETER
The 'self' parameter is a reference to the current instance of the class, and it used to access variables that belongs to the class

It doesnot have to be name 'self' you can call it whatever you like, but it has to be the first parameter of any function in the class...
eg
Use the words mysillyobject and abc instead of self
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def my_func(abc):
        print('Hello my name is ' + abc.name)
p1 = Person('Abubakarr Bah', 23)
p1.my_func()


                    MODIFY OBJECT PROPERTIES
You can modify properties on objects like this 
eg
Set the age of p1 to 40
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def my_func(self):
        print('Hello my name is ' + self.name)
p1 = Person('Abubakarr Bah', 23)
p1.age = 40
print(p1.age)


                        DELETE OBJECTS PROPERTIES
You can delete properties on objects by using the del keyword
eg
Delete the age property from the p1 object 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def my_func(self):
        print('Hello my name is ' + self.name)
p1 = Person('Abubakarr Bah', 23)
del p1.age
print(p1.age)


                        DELETE OBJECT
You can delete objects by using the 'del' keyword
eg
Delete the p1 object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def my_func(self):
        print('Hello my name is ' + self.name)
p1 = Person('Abubakarr Bah', 23)
del p1
print(p1)


                        THE PASS STATEMENT
class definition can not be empty, but if you for some reason have a class definition with no content, put in the 'pass' statement to avoid getting an error...
class Person:
    pass
