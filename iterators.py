                        PYTHON ITERATORS
An iterator is an object that contains a countable number of values

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values

Technically, in python, an iterator is an object which implements the iterator  protocol, which consist of the methods __iter__() and __next__()


                        ITERATOR v ITERABLE
Lists, tuples, dictionaries, and sets are all iterable objects.
They are iterable containers which you get an iterator from

All these objects have a iter() method which is use to get an iterator 
eg
Return an iterator from a tuple, and print each value
mytuple = ('apple', 'banana', 'cherry')
myiter = iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))

Even strings are iterable objects, and can return an iterator
eg
Strings are also iterable objects, containing a sequence of characters
mystr = 'Banana'
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


                            LOOPING THROUGH AN ITERATOR
We can also use a for loop to iterate through an iterable object 
eg
Iterate the values of a tuple
mytuple = ('apple', 'banana', 'cherry')
for x in mytuple:
    print(x)

Iterate the characters of a string 
mystr = 'Banana'
for i in mystr:
    print(i)

The for loop actually creates an iterator and execute the next() method for each loop


                        CREATE AN ITERATOR
To create an object / class as an iterator you have to implement the methods __iter__() and __next__() to your object

As you have learned in the Python Classes/objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created

The __iter__() method acts similar, you can do operation (initializing etc), but most always return the iterator object

The __next__() method also allows you to do operations, and most return the next item in the sequence

eg
Create an iterator that returns numbers, starting with 1, and each sequence will increase by one

class my_nums:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
my_class = my_class()
myiter = iter(my_class)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)



                            STOPITERATION
The example above would continue forever if you have enough next() statement, or if it was used in a for loop

To prevent the iteration to go forever, we can use the stopiteration statement

In the __next__() mehtod, we can add a termination condition to raise an error if the iteration is done a specific number of times

eg
Stop after 20 iteration
class my_numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
my_class = my_numbers()
myiter = iter(my_class)

for x in myiter:
    print(x)