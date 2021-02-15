                        PYTHON INHERITANCE
Inheritance allows us to define a class that inherits all the methods and properties from another class

PARENT CLASS is the class being inherited from, also called base class

CHILD CLASS is the class that inherits from another class, also called derived class

                        CREATE A PARENT CLASS
Any class can be a parent class, so the syntax is the same as creating any other class
eg
Create a class name Person, with fname, lname

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(f'{self.fname} {self.lname}')
x = Person('Bakarr Adonis Bah')
x.printname()


                        CREATE A CHILD CLASS
To create a child class that inherit the functionality from another class, send the parent class a parameter when creating the child class:

eg
Create a class name Student, which will inherit the properties and methods from the person class
class Student(Person):
    pass

NOTE: Use the pass keyword when you do not want to add any other properties and methods from the Person class

class Person:
      def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()



                        ADD THE __INIT__() FUNCTION
So far we have create a child class that inherits the properties and methods from its parent

We want to add the __init__() function to the child class
(instead the pass keyword)
NOTE: The __init__() function is called automatically every time the class is being used to create a new objects

To keep the inheritance from the parents __init__() function, add a call to the parents __init__() function

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(f'{self.fname} {self.lname}')

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
x = Student('Abubakarr', 'Bah')
x.printname()

Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function


                        USE THE SUPER() FUNCTION
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(f'{self.fname} {self.lname}')

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x = Student('Abubakarr', 'Bah')
x.printname()

By using the super() function, you do not have to use name of the parent element, it will automatically inherit the methods and properties from its parent


                    ADD PROPERTIES
Add a property called graduation_year to the Student class

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(f'{self.fname} {self.lname}')

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduation_year = 2019
x = Student('Abubakarr', 'Bah')
print(x.graduation_year)

In the examples below, the year 2019 should be a variable, and passed into the Student class when creating the Student object...
To do so, add another parameter in the __init__() function
eg
Add a year parameter, and pass the correct year when creating objects

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(f'{self.fname} {self.lname}')

class Student(Person):
    def __init__(self, fname, lname, year):
        super.__init__(fname, lname)
        self.graduation_year = year
x = Student('Abubakarr', 'Bah', 2019)
print(x.graduation_year)


                        ADD METHODS
Add a method called welcome to the Student class

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(f'{self.fname} {self.lname}')

class Student(Person):
    def __init__(self, fname, lname, year):
        super.__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print(f'Welcome, {self.fname} {self.lname} to the class of {self.graduation_year}')
x = Student('Abubakarr', 'Bah', 2019)
x.welcome()

If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden