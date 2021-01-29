                        PYTHON SET

myset = {'apple', 'banana', 'cherry'}
SET
Sets are used to store multiple items in a single variable
Set is one of the 4 built-in data types in python use to store collection of data types, the other three are list, tuple, dict different usage and qualities

Set is collection which is both unordered and unindexed
Sets are written with curl brackets

myset = {'apple', 'banana', 'cherry'}
print(myset)


                            SET ITEMS
Sets items are unordered, unchangeable, and do not allow duplicate values


                            UNORDERED
Unordered means that the items in a set do not have a define order
Set items can appear in a different order every time you use them, and cannot be referred to by index or key


                            UNCHANGEABLE
Sets are unchangeable, meaning that we cannot change the item after the set has been created
NOTE: Once the set is created, you cannot change its items, but you can add new items


                            DUPLICATE NOT ALLOWED
Sets cannot have two items with the same name 
myset = {'apple', 'banana', 'cherry', 'apple'}
print(myset)


                            GET THE LENGTH OF A SET
To determine how many items a set has, use the len() function
myset = {'apple', 'banana', 'cherry'}
print(len(myset))


                            SET ITEMS -DATA TYPES
Set items can be any data type 
eg
string, int, float, bool
set1 = {'apple', 'banana', 'cherry'}
set2 = {1, 2, 3, 4, 5}
set3 = {True, False, True}
print(set1)
print(set2)
print(set3)
A set can contain different data types
set1 = {'abc', 34, True, 30.1, 'male'}
print(set1)


                                TYPE()
From python perspective, set are defined as objects with the data type 'set'
myset = {'apple', 'banana', 'cherry'}
print(type(myset))


                                THE SET CONSTRUCTOR
It also possible to use the set() constructor to make a set
myset = set(('apple', 'banana', 'cherry'))
print(myset)



                                PYTHON - ACCESS SET ITEMS
You cannot access items in a set by referring to an index or a key
But you can loop through the set items using a 'for' loop or ask if a specified value is present in a set, by using the 'in' keyword
eg
Loop through the set and print the value
myset = {'apple', 'banana', 'cherry'}
for x in myset:
    print(x)
eg
check if 'banana' is present in the set
myset = {'apple', 'banana', 'cherry'}
if 'banana' in myset:
    print('Yes it present')
or
print('banana' in myset)


                                CHANGE ITEMS
Once a set is created, you cannot change, but you can add new items


                                PYTHON ADD SET ITEMS
Once a set is created, you cannot change, but you can add new items
To add one item to a set use the add() method 
myset = {'apple', 'banana', 'cherry'}
myset.add('orange')
print(myset)


                                ADD SET
To add items from another set into the current set, use the update() method 
myset = {'apple', 'banana', 'cherry'}
tropical = {'pineapple', 'orange', 'melon'}
myset.update(tropical)
print(myset)


                                ADD ANY ITERABLE
The object in the update() method does not have to be a set, it can be any iterable object (tuple, list,dict)
myset = {'apple', 'banana', 'cherry'}
tropical = ['pineapple', 'orange', 'melon']
myset.update(tropical)
print(myset)


                                PYTHON REMOVE SET ITEMS
To remove an item in a set, use the remove() method, or the discard () method
myset = {'apple', 'banana', 'cherry', 'orange'}
myset.remove('orange')
print(myset)
NOTE: If the item to remove does not exists, the remove () method will raise an error

myset = {'apple', 'banana', 'cherry', 'orange'}
myset.discard('orange')
print(myset)
NOTE: If the item to remove does not exists, discard() will NOT raise an error
You can also use the pop() method to remove an item but this method will remove the last item.. Remember that sets are unordered, so you will not know what item that gets removed
myset = {'apple', 'banana', 'cherry', 'orange'}
myset.pop()
print(myset)

The clear() method empties the set
myset = {'apple', 'banana', 'cherry', 'orange'}
myset.clear()
print(myset)

The 'del' keyword will delete the set completely
myset = {'apple', 'banana', 'cherry', 'orange'}
del myset
print(myset)



                                PYTHON LOOP SETS
You can loop through the set items by using the for loop
myset = {'apple', 'banana', 'cherry', 'orange'}
for x in myset:
    print(x)


                                PYTHON JOIN SETS
JOIN TWO SETS
There are several ways to join two or more sets in python
You can use the union() method that returns a new set containing all the items from both sets, or the update() method that inserts all the items from one set into another
eg
The union() method returns a new set with all items from both side
set1 = {'apple', 'banana', 'cherry'}
set2 = {1, 2, 3, 4, 5}
set3 = set1.union(set2)
print(set3)

set1 = {'apple', 'banana', 'cherry'}
set2 = {1, 2, 3, 4, 5}
set3 = set1.update(set2)
print(set3)
NOTE: The update() and union() will exclude any duplicate item


                                KEEP ONLY THE DUPLICATE
The intersection_update() method will keep only the items that are present in both side
set1 = {'apple', 'banana', 'cherry'}
set2 = {'apple', 'google', 'microsoft'}
set1.intersection_update(set2)
print(set1)
NOTE: Keep the items that exists in both set set1 and set2 

The intersection() method will returns a new set that contain the items that are in both sets
set1 = {'apple', 'banana', 'cherry'}
set2 = {'apple', 'google', 'microsoft'}
set3 = set1.intersection(set2)
print(set3)


                            KEEP ALL, BUT NOT THE DUPLICATE
The symmetric_difference_update() method keep only the elements that NOT present in both set
eg
Keep the items that are not present in both sets
set1 = {'apple', 'banana', 'cherry'}
set2 = {'apple', 'google', 'microsoft'}
set3 = set1.symmetric_difference_update(set2)
print(set3)

The symmetric_difference() method will return a new set
that contains only the elements that NOT present in both set
Returns a set that contains all items from both sets, except items that are present in both 
set1 = {'apple', 'banana', 'cherry'}
set2 = {'apple', 'google', 'microsoft'}
set3 = set1.symmetic_difference(set2)
print(set3)



                            PYTHON SET METHODS

METHOD                          DESCRIPTION

add()                           Adds an elements to the set

clear()                         Removes all elements from the set

copy()                          Returns a copy of the set

difference()                    Returns a set containing the difference between two
                                or more sets

difference_update()             Removes the items in this set that are also included
                                in another specified item

discard()                       Removes the specified item

intersection()                  Returns a set, that is the intersection of two
                                other sets

intersection_update()           Removes the items in this set that are not present
                                in other, specified set

isdisjoin()                     Returns whether two set have a intersection or not

issubset()                      Returns whether this set contains another set or not

pop()                           Removes an element from the set

remove()                        Removes the specified element

symmetric_difference()           Returns a set with the symmetic difference of
                                 two sets

symmetric_difference_update()     Inserts the symmetric differences from this
                                  set to another

union()                         Returns a set containing the union of sets

update()                        Update the set with the union of this set and others