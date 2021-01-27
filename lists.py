                            PYTHON LIST
Lists are used to store multiple items in one variable

Lists are one of the four built-in data types in Python
Used to store collection of data, the other three are Set,Tuple,and Dictionary
all with different qualities and usage

List are created using square brackets []
eg
fruits = ['apple', 'banana', 'cherry']
print(fruits)

 
                                LIST ITEMS
List items are ordered, changeable and allow duplicate values
List items are indexed, the first item has index[0]
the second item has index[1]


                            ORDERED
When we say the list is ordered, it means that the items have a defined other, and that order will not change
If you add a new item to the list, the new item will placed at the end of the list
NOTE: There are some list methods that will change the order, but in general the order of the items will not change


                            CHANGEABLE
The list is changeable, meaning that we can change, add and remove items in a list after it has been created

   
                            ALLOW DUPLICATE
Since lists are indexed, lists can have items with the same name
The list allows duplicate values
eg
fruits = ['apple', 'banana', 'cherry', 'apple', 'banana']
print(fruits)
 

                            LIST LENGTH
To determine how many items the list has, use the len() function
fruits = ['apple', 'banana', 'cherry']
print(len(fruits))


                            LIST ITEMS - DATA TYPES
List items can be any data type: It can be strings, int, float, booleans
list1 = ['apple', 'banana', 'cherry']
list2 = [1, 2, 3, 4]
list3 = [True, False, True]
print(list1)
print(list2)
print(list3)

A list can contain different data types
A list with string, integer and boolean values
list1 = ['abc', 34, True, 'male']
print(list1)


                            TYPE()
From python perspective lists are defined as objects with the data type of list
<class 'list'>
What is the data type of a list
fruits = ['apple', 'banana', 'cherry']
print(type(fruits))


                            THE LIST CONSTRUCTOR
It is also possible to use the list constructor when creating a new list
Use the list constructor to make a new list
fruits = list(('apple', 'banana', 'cherry'))
print(fruits)


                        PYTHON COLLECTIONS (ARRAYS)
There are four collection data types in the Python Programming Language
LIST - is a collection which is ordered and changeable
Allow duplicate members

TUPLE - is a collection which is ordered and unchangeable
Allow duplicate members

SET - is a collection which is unordered and indexed
No duplicate members

DICTIONARY - is a collection which is unordered and unchangeable
No duplicate members

When choosing a collection type, it is useful to understand the properties of that type..
Choosing the right type for a particular data set could mean retention of meaning, and it could mean an increasing in efficiency or security



                        PYTHON - ACCESS LIST ITEMS
ACCESS ITEMS
List items are indexed and you can access them by referring to the index number
eg
Print the second item of the list
fruits = ['apple', 'banana', 'cherry']
print(fruits[1])
NOTE: The first item has index 0


                        NEGATIVE INDEXING
Negative indexing means start from the end
-1 refers to the last item -2 refers to the second last item etc
fruits = ['apple', 'banana', 'cherry']
print(fruits[-1])


                        RANGE OF INDEXES
You can specify a range of indexes by specifying where to start and where to end the range
When specifying a range, the return value will be a new list with the specified items
eg
Return the third, fourth, fifth item
fruits = ['apple', 'banana', 'cherry']
print(fruits[2:5])
NOTE: The search starts at index 2 (included )and end at index 5 (not included)

By leaving out the start index or the start value the range will start at the first item to, but NOT including 'kiwi'
fruits = ['apple', 'banana', 'cherry','kiwi', 'orange', 'melon']
print(fruits[:4])

By leaving out the end value, the range will go to the end of the list
fruits = ['apple', 'banana', 'cherry','kiwi', 'orange', 'melon', 'mango']
print(fruits[2:])


                        RANGE OF NEGATIVE INDEXES
Specifying negative indexes if you want to start the search from the end of the list
eg
This retruns the items from 'orange'(-4) to, but NOT including 'mango'(-1)
fruits = ['apple', 'banana', 'cherry','kiwi', 'orange', 'melon', 'mango']
print(fruits[-4:-1])


                        CHECK IF ITEMS EXISTS
To determine if a specified item is present in a list use the 'in' keyword
fruits = ['apple', 'banana', 'cherry']
if 'apple' in fruits:
    print('Yes Apple is present in the list')



                        PYTHON - CHANGE LIST ITEMS
To change the value of a specified item, refer to the index number
eg
Change the second item
fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'mango'
print(fruits)


                        CHANGE A RANGE OF ITEM VALUES
To change the value of items within a specified range define a list with the new values, and refer to the range of index numbers where you want to insert the new values
Change the values 'banana' and 'cherry' with the values 'mango', and 'lemon'
fruits = ['apple', 'banana', 'cherry']
fruits[1:3] = ['mango', 'lemon']
print(fruits)

If you insert more items than you replace, the new items will inserted where you specified, and the remaining items will move accordingly
Change the second value by replacing it with two new values
fruits = ['apple', 'banana', 'cherry']
fruits[1:2] = ['mango', 'orange']
print(fruits)
NOTE: The length of the list will change when the number of items inserted doesnot match the number of items replaced

If you insert less items than you replace, the mew item will be inserted where you specified, and the remaining items will move accordingly
eg
Change the second and third value by replacing it with one value
fruits = ['apple', 'banana', 'cherry']
fruits[1:3] = ['melon']
print(fruits)


                            INSERT ITEMS
To insert a new list item, without replacing any of the existing values, we can use the insert() method 
The insert() method inserts an item at the specified index
eg
Insert watermelon as the third item
fruits = ['apple', 'banana', 'cherry']
fruits.insert(2, 'watermelon')
print(fruits)
NOTE: As a result of the example above, the list will now contain 4 items



                            PYTHON - ADD LIST ITEMS
APPENDS ITEMS
To add an item at the end of the list, use the append() method
eg
Using the append() method to append an item 
fruits = ['apple', 'banana', 'cherry']
fruits.append('lemon')
print(fruits)


                            INSERT ITEMS
To insert a list item at a specified index, use the insert() method 
The insert() method inserts an item at the specified index
eg
Insert an item as the second position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'lemon')
print(fruits)


                            EXTEND LIST
To append elements from another list to the current list, use the extend() method
eg
Add the elements of tropical to fruits
fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'lemon']
fruits.extend(tropical)
print(fruits)
The elements will be added to the end of the list


                        ADD - ANY - ITERABLE
The extend() method doesnot have to append lists, you can add any iterable object
(tuples, sets, dictionary)
eg
Add elements of a tuple to a list
fruits = ['apple', 'banana', 'cherry]
thistuple = ('kiwi', 'orange')
fruits.extend(thistuple)
print(fruits)



                        PYTHON REMOVE LIST ITEMS
REMOVE SPECIFIED ITEM
The remove() method removes the specified item 
eg
Remove 'banana'
fruits = ['apple', 'banana', 'cherry]
fruits.remove('banana')
print(fruits)

                        REMOVE SPECIFIED INDEX
The pop() method removes the specified index
eg
Remove the second index
fruits = ['apple', 'banana', 'cherry]
fruits.pop(1)
print(fruits)
If you do not specified the index the pop() method removes the last item
Remove the last item
fruits = ['apple', 'banana', 'cherry]
fruits.pop()
print(fruits)

The 'del' keyword also remove the specified index
eg
Remove the first item
fruits = ['apple', 'banana', 'cherry]
del fruits[0]
print(fruits)

The 'del' keyword can also delete the list completely 
eg
Delete the entire list
fruits = ['apple', 'banana', 'cherry]
del fruits
print(fruits)

                    CLEAR THE LIST
The clear() method empties the list
The list still remain but has no content
eg
Clear the list content
fruits = ['apple', 'banana', 'cherry]
fruits.clear()
print(fruits)



                    PYTHON LOOP LIST
LOOP THROUGH A LIST
You can loop through a list items by using a for loop 
eg
Print all items in the list one, by one
fruits = ['apple', 'banana', 'cherry]
for x in fruits:
    print(x)


                    LOOP THROUGH THE INDEX NUMBERS
You can also loop through the list items by referring to their index numbers
Use the range() and len() functions to create a suitable iterable
eg
Print all items by referring to their index numbers
fruits = ['apple', 'banana', 'cherry]
for x in range(len(fruits)):
    print(x)
The iterable created in the example above is [0, 1, 2]


                    USING A WHILE LOOP
You can loop through the list items by using the while loop
Use the len() function to determine the length of the list
Then start at 0 and loop your way through the list items by referring to their indexes
Remember to increase the index by 1 after each iteration
eg
Print all items, using while loop to go through all the index numbers
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


                        LOOPING USING LIST COMPREHENSION
List comprehension offers the shortest syntax for looping through lists
eg
A short for loop that will print all items in a list
fruits = ['apple', 'banana', 'cherry]
[print(x) for x in fruits]



                        PYTHON LIST COMPREHENSION
LIST COMPREHENSION
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
eg
Based on a list of fruits, you want a new list containing only the fruits with the letter 'a' in the name
Without list comprehension you will have to write a for statement with a condition test inside
fruits = ['apple', 'banana', 'cherry]
newlist = []
for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)

With list comprehension you can do that with only oneline of code
fruits = ['apple', 'banana', 'cherry]
newlist = [x for x in fruits if 'a' in x]
print(newlist)

                        THE SYNTAX
newlist = [expression for item in iterable if condition == True]
The return value is a new list leaving the old list unchange

                        CONDITION
The condition is like a filter that only accepts the items that valuate to True
eg
Only accept items that are not 'apple'
fruits = ['apple', 'banana', 'cherry]
newlist = [x for x in fruits if x != 'apple']
print(newlist)

The condition if x != 'apple' will return True for all elements other than 'apple' making the newlist contain all fruits except 'apple'


                        ITERABLE
The iterable can be any iterable object, like a list, tuple, set etc
eg
You can use the range() function to create an iterable
newlist = [x for x in range(10)]
print(newlist)

Same example, but with a condition 
eg
Accept only numbers lower than 5
newlist = [x for x in range(10) if x < 5]
print(newlist)


                        EXPRESSION
The expression is the current item in the iteration, but it is also the outcome, what you can manipulate before it ends up like a list item in the newlist
eg
fruits = ['apple', 'banana', 'cherry]
newlist = [x for x in fruits]
print(newlist)

eg
Set all values in the newlist to 'hello'
newlist = ['hello' for x in fruits]
The expression can also contain condition, not like a filter, but as a way to manipulate the outcome
eg
Return 'Orange' instead of 'banana'
fruits = ['apple', 'banana', 'cherry]
newlist = [x if x != 'banana' else 'Orange' for x in fruits]
print(newlist)

The expression in the example above says 
Return the item if is not 'banana', if it is 'banana' return 'Orange'



                        PYTHON SORT LIST
SORT LIST ALPHANUMERICALLY
List objects have a sort() method that will sort the list alphanumerically ascending, by default
eg
Sort the list alphanumeric 
fruits = ['apple', 'banana', 'cherry]
fruits.sort()
print(fruits)

eg
Sort the list numerically
nums = [100, 50, 65, 82, 32]
nums.sort()


                        SORT DESCENDING
To sort descending, use the keyword argument reverse = True
eg
Sort the list descending
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'pineapple', 'melon']
fruits.sort(reverse = True)

eg
Sort the list descending
nums = [100, 50, 65, 82, 32]
nums.sort(reverse = True)


                        CUSTOMIZE SORT FUNCTION
You can also customize your own function by using the keyword argument key = function
The function will return a number that will be use to sort the list (the lowest number first)

Sort the list based on how close the number is to 50
def myfunc():
    return abs(n - 50)
nums = [100, 50, 65, 82, 32]
nums.sort(key = myfunc)
print(nums)

                        CASE INSENSITIVE SORT
By default the sort() method is case - sensitive, resulting in all capital letters being sorted before lower case letters
eg
Case - sensitive sorting can give an unexpected result
fruits = ['apple', 'Orange', 'Kiwi', 'cherry']
print(fruits)

Luckily we can use built-in function as key functions when sorting a list
So if you want a case - sensitive sort function, use str.lower as key function
fruits = ['apple', 'Orange', 'Kiwi', 'cherry']
fruits.sort(key = str.lower)
print(fruits)


                        REVERSE ORDER
What if you want to reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements 
eg
Reverse the order of the list items
fruits = ['apple', 'Orange', 'Kiwi', 'cherry']
fruits.reverse()
print(fruits)



                        PYTHON - COPY LISTS
COPY A LIST
You cannot copy a list simply by typing list2 = list1 because: list2 will onl be a reference to list1, and changes made in list1 will automatically also made i list2

The are ways to make a copy, one way is to use the built-in method copy()
eg
Make a copy of a list with the copy() method 
fruits = ['apple', 'Orange', 'Kiwi', 'cherry']
new_fruits_list = fruits.copy()
print(new_fruits_list)

Another way to make a copy is to use the built-in method list()
eg
Make a copy of a list with the list() method
fruits = ['apple', 'Orange', 'Kiwi', 'cherry']
new_fruits_list = list(fruits)
print(new_fruits_list)



                            PYTHON - JOIN LISTS
JOINT TWO LISTS
There are several ways to join, or concatenate, two or more lists in Python
One of the easiest ways are by using the + operator
eg
Join two list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

Another way to join two lists are by appending all the items from list2 into list1, one by one
eg
Append list2 into list1
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

Or you can use the extend() method, which purpose is to add elements from one list to another list
eg
Use the extend() method to add list2 at the end list1
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)



                    PYTHON - LIST METHODS
METHOD                      DESCRIPTION
append()                    Adds an element at the end of the list

clear()                     Removes all the elements from the list

copy()                      Returns the number of elements with the specified values

extend()                    Add the elements of a list(or any iterable to the
                            end of the current list)

index()                     Returns the index of the first element with
                            the specified value

insert()                    Add an element at the specified position

pop()                       Removes the element at the specified position

remove()                    Removes the item with specified value

reverse()                   Reverse the order of the list

sort()                      Sorts the list