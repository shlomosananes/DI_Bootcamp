print("\n--- Exercise 1: Currencies ---\n")

"""
Exercise 1: Currencies
Instructions
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #Your code starts HERE


Using the code above, implement the relevant methods and dunder methods which will output the results below.
Hint : When adding 2 currencies which don’t share the same label you should raise an error.
>>> c1 = Currency('dollar', 5)
>>> c2 = Currency('dollar', 10)
>>> c3 = Currency('shekel', 1)
>>> c4 = Currency('shekel', 10)

>>> str(c1)
'5 dollars'

>>> int(c1)
5

>>> repr(c1)
'5 dollars'

>>> c1 + 5
10

>>> c1 + c2
15

>>> c1 
5 dollars

>>> c1 += 5
>>> c1
10 dollars

>>> c1 += c2
>>> c1
20 dollars

>>> c1 + c3
TypeError: Cannot add between Currency type <dollar> and <shekel>
"""

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return int(self.amount)


    def __add__(self, val):
        try:
            if isinstance(val, Currency):
                if self.currency == val.currency:
                    return self.amount + val.amount
                else:
                    raise ValueError()
            else:
                return f'{self.amount + val}'
        except:
            return f'TypeError: Cannot add between Currency type <{self.currency}> and <{val.currency}>'


    def __iadd__(self, val):    # The outputs must be     (1) return self     (2) ERROR
        try:
            if isinstance(val, Currency):
                if self.currency == val.currency:
                    self.amount += val.amount
                    return self
                else:
                    raise ValueError()
            else:
                self.amount += val
                return self
        except:
            return f'TypeError: Cannot add between Currency type <{self.currency}> and <{val.currency}>'


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)

print(c1)
c1 += 5
print(c1)

c1 += c2
print(c1)

c1 += c3
print(c1)





print("\n--- Exercise 2: Import ---\n")

"""
Instructions
In a file named func.py create a function that adds 2 number, and prints the result
In a file namedexercise_one.py import and the function
Hint: You can use the the following syntaxes:
import module_name 
OR 
from module_name import function_name 
OR 
from module_name import function_name as fn 
OR
import module_name as mn
"""





print("\n--- Exercise 3: String Module ---\n")

"""
Exercise 3: String Module
Instructions
Generate random String of length 5
Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
Hint: use the string module
"""

import random
import string

print(''.join(random.choices(string.ascii_letters, k=5)))





print("\n--- Exercise 4: Current Date ---\n")

"""
Exercise 4 : Current Date
Instructions
Create a function that displays the current date.
Hint : Use the datetime module.
"""
# datetime is a built-in Module
# what comes after the from is the module
# what comes after the import is the class
# there is a module named datetime and a class named datetime.
# According to python guidelines in PEP 8, the class should be named Datetime
# If we write only 'import datetime' we will import the whole Module
# In this case, when calling the classe 'datetime' we must write datetime.datetime_____
# We can use 'alias' to avoid confusion

from datetime import date as Date, timedelta as TimeDelta, datetime as DateTime
from datetime import datetime

def today():
    today = Date.today()
    print(today)

today()





print("\n--- Exercise 5: Amount of Time Left Until January 1st ---\n")

"""
Exercise 5 : Amount Of Time Left Until January 1st
Instructions
Create a function that displays the amount of time left from now until January 1st.
(Example: the 1st of January is in 10 days and 10:34:01hours).
"""

# import datetime
#
# x = datetime.datetime.now()
# print(x)
#
# Date Output
# When we execute the code from the example above the result will be:
#
# 2024-03-12 18:57:46.661598
# The date contains year, month, day, hour, minute, second, and microsecond.
#
# The datetime module has many methods to return information about the date object.
#
# Here are a few examples, you will learn more about them later in this chapter:
# Return
# the
# year and name
# of
# weekday:
#
# import datetime
#
# x = datetime.datetime.now()
#
# print(x.year)
# print(x.strftime("%A"))

# CREATING DATE OBJECTS
# To create a date, we can use the datetime() class (constructor) of the datetime module.
#
# The datetime() class requires three parameters to create a date: year, month, day.
#
# import datetime
#
# x = datetime.datetime(2020, 5, 17)
#
# print(x)


# CLASS timedelta
# Includes several arguments (with default value = 0) such as:
#### weeks
#### days
#### hours
#### minutes
#### seconds
#### miliseconds
#### microseconds


# t1 = TimeDelta(1,1,1)
# print(t1)
# t2 = TimeDelta(2,2,2)
# print(t2)

def time_left_to_Jan01():
    today = Date.today()
    year = today.year
    target = Date(year + 1, 1,1)
    days = target - today
    print(days)

time_left_to_Jan01()





print("\n--- Exercise 6: Birthday And Minutes ---\n")

"""
Exercise 6 : Birthday And Minutes
Instructions
Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.
"""

def minutes_lived():
    today = DateTime.now()
    birthday = input("Enter your birthday separating D M Y by a single space: ")
    birthday_data = birthday.split()
    birthdate = DateTime(int(birthday_data[2]),int(birthday_data[1]),int(birthday_data[0]))
    minutes_lived = ((today - birthdate).total_seconds()) / 60
    print(minutes_lived)

minutes_lived()





print("\n--- Exercise 7: Faker Module ---\n")

"""
Exercise 7 : Faker Module
Instructions
Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
Create an empty list called users. Tip: It should be a list of dictionaries.
Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.
"""

# Need to install package 'faker'.
# When writing from faker import faker, the Pycharm will ask if we want to install the package.

from faker import Faker
fake = Faker()

users = []

" { name : 'John' , address : 'Frishman 16' , language_code : 'python' } "

def add_users():
    dictio = {
        'name' : fake.name() ,
        'address1' : fake.address() ,
        'langage_code' : '?'
    }
    users.append(dictio)

add_users()
add_users()
add_users()
add_users()
add_users()

print(users)

