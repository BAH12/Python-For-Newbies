                                PYTHON ARRAYS
NOTE: Python doesnot have a build-in support for arrays, but python list can be use instead

                                ARRAYS
NOTE: This page shows you how to use list and arrays however, to work with arrays in python you will have to import a library like the NumPy library

Arrays are used to store multiple values in one single variable

eg
create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]


                                WHAT IS AN ARRAY
An array is a special variable, which can hold more than one value at a time
If you have a list of items(a list of car names for example), storing the cars in a single variable could look like this
car1 = "Ford"
car2 = "Volvo"
cars3 = "BMW"

However, what if you want to loop through the cars and find a specific one? And what if you had not 3 but 300
The solution is an Array
An array can hold many values under a single variable and you can access the values by referring to the indexing number


                            ACCESS THE ELEMENTS OF AN ARRAY
You refer to an array element by referring to the index number
eg
Get the first element of the array
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

MODIFY the value of the first array item
cars[0] = 'Toyota'


                            THE LENGTH OF AN ARRAY
Use the len() method to return the length of an array (The number of elements in the cars array)
eg
Return the number of elements in the cars array
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)


                            LOOPING ARRAY ELEMENTS
You can use the 'for in' loop to loop through all the elements of an array
eg
Print each item in the cars array
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)


                            ADDING ARRAY ELEMENTS
You can use the append() method to add an elements to an array 
eg
Add one more element to the cars array
cars = ["Ford", "Volvo", "BMW"]
cars.append('Honda')
print(cars)


                            REMOVING ARRAY ELEMENTS
You can use the pop() method to remove an element from the array
eg
Delete the second element of the cars array
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)

You can also use the remove() method to remove an element from the array
eg
Delete the element that has the value 'Volvo'
cars = ["Ford", "Volvo", "BMW"]
cars.remove('Volvo')

NOTE:The lists remove() method only removes the first occurrence of the specified value


                                ARRAY METHODS
Python has a set of build-in methods that you can use on lists/arrays

METHOD              DESCRIPTION
append()            Adds an element at the end of the list

clear()             Removes all the elements from the list

copy()              Returns a copy of the list

count()             Returns the number of elements with the specified value

extend()            Add the elements of a list(or any iterable), to the end
                    of the current list

index()             Returns the index of the first element with
                    the specified value

insert()            Adds an element at the specified position

pop()               Removes the element at the specified position

remove()            Removes the first item with the specified value

reverse()           Reverse the order of the list

sort()              Sort the list