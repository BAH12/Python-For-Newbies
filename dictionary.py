                        PYTHON DICTIONARY
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
print(mydict)

Dictionaries are used to store data values in key: value pairs
A dictionary is a collection which is unordered, changeable and doesnot allow duplicate values
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
print(mydict)


                            DICTIONARY ITEMS
Dictionary items are unordered, changeable and doesnot not allow duplicate.. 
Dictionary items are present in key: value pairs, and can be referred to by using the key name
eg
Print the 'brand' value of the dictionary
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
print(mydict['brand'])


                            UNORDERED
When we said that dictionaries are unordered, it means that the items doesnot have a define order, you cannot refer to an item by using an index


                            CHANGEABLE
Dictionaries are changeable, it means that we can change, add, and remove an item after the dictionary has been created


                            DUPLICATE NOT ALLOWED
Dictionaries cannot have two items with the same name
eg
Duplicate values will overwrite existing values:
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964,
    'year': 2021
}
print(mydict)


                            DICTIONARY LENGTH
To determine how many items a dictionary has use the len () function
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
print(len(mydict))


                            DICTIONARY ITEMS - DATA TYPES
The values in dictionaries can be of any data type
eg
string, int, float, bool, and list data types

mydict2 = {
    'brand': 'ford',
    'electric': False,
    'year': 2021,
    'color': 'red'
}
print(mydict2)


                             TYPE()
From Python perspective, dictionaries are defined as objects with the data type 'dict'
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
print(type(mydict))


DICTIONARY is a collection which is unordered, changeable and no duplicate values


                            ACCESS DICTIONARY ITEMS
ACCESS ITEMS
You can access the items of a dictionary by referring to it keys name, inside square brackets
eg
get the value of the 'model' key:
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
print(mydict['model'])
There is also a method called get() that will give you the same result
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
print(mydict.get('model'))


                            GET KEYS
The keys() method will return a list with all the keys in the dictionary
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
x = mydict.keys()
print(x)

The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
x = mydict.keys()
print(x) # before the change
mydict['color'] = 'red'
print(x) # after the change


                            GET VALUES
The values() mehtod will return a list of all the values in the dictionary
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
x = mydict.values()
print(x)

The list of the values in a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the dictionary
x = mydict.values
print(x) # before the change
mydict['year'] = 2021
print(x) # after the change


                                GET ITEMS
The item() method will return each item in a dictionary as tuples in a list
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
x = mydict.items()
print(x) 
The returned list is a view of items of the dictionary meaning that any changes done to the dictionary will be reflected in the items list
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
x = mydict.items()
print(x) # before the change
mydict['year'] = 2021
print(x) # after the change


                                CHECK IF KEY EXISTS
To determine if a specified key is present in a dictionary use the 'in' keyword
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
if 'model' in mydict:
    print('Yes')


                                CHANGE DICTIONARY ITEMS
CHANGE VALUES
You can change the value of a specific item by referring to it key name:
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
mydict['year'] = 2021
print(mydict)


                                UPDATE DICTIONARY
The update() method will update the dictionary with the items from the given argument
The argument must be a dictionary, or an iterable object with key: value pairs
eg
update the 'year' of the mydict by using the update() method
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
mydict.update({'year': 2021})
print(mydict)


                                ADD DICTIONARY ITEMS
ADDING ITEMS
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
mydict['color'] = 'white'


                                UPDATE DICTIONARY
The update() method will update the dictionary with the items from a given argument.
If the item doesnot exists, the item will be added
The argument must be a dictionary or an iterable object with key:value pairs
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
mydict.update({'year': 2021})
print(mydict)


                            REMOVE DICTIONARY ITEMS
REMOVING ITEMS
There are several methods to remove items from a dictionary

The pop() method removes the item with the specified key name
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
mydict.pop('model')
print(mydict)

The popitem() method removes the last inserted item (in version 3.7, a random  item is removed instead)
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
mydict.popitem()
print(mydict)

The 'del' keyword removes the item with the specified key name
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
del mydict['model']
print(mydict)
The 'del' keyword can delete the dictionary completely 
del mydict
print(mydict)

The clear() method empties the dictionary
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
mydict.clear()
print(mydict)


                                LOOP DICTIONARIES
LOOP THROUGH A DICTIONARY
You can loop through a dictionary by using the 'for' loop
When looping through a dictionary, the return values are the keys of the dictionary,
but there is a method to return the values as well
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
for x in mydict:
    print(x)

print all values in the dictionary one by one
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
for i in mydict:
    print(mydict[i])

You can also use the values() method to return the values of a dictionary
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
for x in mydict.values():
    print(x)

You can also use the keys() method to return the keys of a dictionary
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
for i in mydict.keys():
    print(i)

Loop through both keys and values, by using the items() method 
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
for x, y in mydict.items():
    print(x, y)


                        COPY DICTIONARIES
COPY A DICTIONARY
You cannot copy a dictionary simply by typing
dict1 = dict2
because dict2 will only be reference to dict1, and changes made in dict2 will automatically also made in dict1
The are ways to make a copy, one way is to use the built-in dictionary copy() method

Make a copy of a dictionary with the copy() method 
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
mydict2 = mydict.copy()
print(mydict2)

Another way to make a copy is to use the built-in function dict()
make a copy of a dictionary with the dict() function
mydict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
mydict3 = dict(mydict)
print(mydict3)


                        NESTED DICTIONARIES
A dictionary can contain dictionaries, this is called nested dictionaries
eg
Create a dictionary that contain three dictionaries
my_family = {
    'child1':{'name': 'Emil', 'year': 2004},
    'child2':{'name': 'Tobias', 'year': 2007},
    'child3':{'name': 'Linux', 'year': 2011}
}
Or, if you want to add three dictionaries in to a new dictionary
eg
Create three dictionaries then create one dictionary that will contain the other three dictionaries
child1 = {'name': 'Emil', 'year': 2004}
child2 = {'name': 'Tobias', 'year': 2007}
child3 = {'name': 'Linux', 'year': 2011}
my_family = {
    'child1':child1,
    'child2':child2,
    'child3':child3
}


                            PYTHON DICTIONARY METHODS

METHOD                  DESCRIPTION

clear()                 Removes all the elements from the dictionary

copy()                  Returns a copy of the dictionary

fromkeys()              Returns a dictionary with the specified keys and values

get()                   Returns the value of the specified key

items()                 Returns a list containing a tuple for each key value pair

keys()                  Returns a list containing the dictionary's keys

pop()                   Removes the elements with the specified key

popitem()               Removes the inserted key-value pair

setdefault()            Returns the value of the specified key. If the key
                        doesnot exist: Insert the key with the specified value

update()                Update the dictionary with the specified key-value-pair

values()                Returns a list of all the values in the dictionary
