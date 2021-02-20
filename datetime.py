                                PYTHON DATETIME
A date in python is not a data type of its own, but we can import a module named datetime to work with dates as date objects
eg
Import the datetime module and display the current date

import datetime
x = datetime.datetime.now()
print(x)

                                DATE OUTPUT
When we execute the code from the example above the result will be the current year, month, day, hour, minute, second, and microsecond

The datetime module has many methods to return information about the date object

Here are a few example, you will learn more about later in the chapter
eg
Return the year and name of the weekday
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime('%A'))


CREATE DATE OBJECTS
To create a date, we can use the datetime() class (constructor) of the datetime
module

The datetime() class requires three parameters to create a date: year, month, day
eg
Create a date Object

import datetime
x = datetime.datetime.now(2021, 02, 20)
print(x)

The datetime() class also takes parameters for time and timezone(hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0,(none for timezone)


                                THE STRFTIME() METHOD
The datetime object has method for formatting date objects into readable strings
The method is called strftime(), and takes one parameter, format specify the format of the returned string
eg
Display the name of the month 

import datetime
x = datetime.datetime(2021, 02, 20)
print(x.strftime('%B'))


A reference of all the legal format codes

DIRECTIVE           DESCRIPTION                                 EXAMPLE

%a                  Weekday, short version                      Wed

%A                  Weekday, full version                       Wednesday

%w                  Weekday as number 0 - 6, 0 is sunday        3

%d                  Day of the month 01 - 31                    31

%b                  Month name, short version                   Dec

%B                  Month name, full version                    December

%m                  Month as a number 01 - 12                   12

%y                  Year,short version,without century          18

%Y                  Year, full version                          2021

%H                  Hour 00 - 23                                17

%I                  Hour 00 - 12                                05

%p                  AM/PM                                       PM

%M                  Minute 00 - 59                              41

%S                  Second 00 - 59                              08

%f                  Microsecond 000000 - 999999                  548513

%z                  UTC offset                                  + 0100

%Z                  Timezone                                    CST

%U                  Week number of year,Sunday                  52
                    as the first day of the week, 00 - 53

%W                  Week number of year,Monday as the 
                    first of week, 00 - 53                       52

%c                  Local version of date and time                Mon Dec
                                                                17:41:00 2021

%x                  Local version of date                       02/20/2021

%X                  Local version of time                       17:43:00

%%                  A % character                                %

%G                  ISO 8601 year                                2021

%u                  ISO 8601 Weekday (1 - 7)                     1

%V                  ISO 8601 Week number (01 - 53)                1



