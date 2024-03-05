"""
Exercise 1 : Convert Lists Into Dictionaries
Instructions
Convert the two following lists, into dictionaries.
Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
"""

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(values)
diction = dict(zip(keys, values))
print(diction)

"""
Exercise 2 : Cinemax
Instructions
A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.
Given the following object:
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
How much does each family member have to pay ?
Print out the family’s total cost for the movies.
Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
"""

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
prices = family.copy()

for person, age_to_cost in prices.items():
    if age_to_cost < 3:
        age_to_cost = 0
    elif age_to_cost <= 12:
        prices[person] = 10
    else:
        prices[person] = 15

print(f"Prices per family member >  {prices}")

total_price = sum(prices.values())
print(f"The total cost for the family is: {total_price}")

"""
Exercise 3: Zara
Instructions
Here is some information about a brand.
name: Zara 
creation_date: 1975 
creator_name: Amancio Ortega Gaona 
type_of_clothes: men, women, children, home 
international_competitors: Gap, H&M, Benetton 
number_stores: 7000 
major_color: 
    France: blue, 
    Spain: red, 
    US: pink, green


2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
3. Change the number of stores to 2.
4. Print a sentence that explains who Zaras clients are.
5. Add a key called country_creation with a value of Spain.
6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
7. Delete the information about the date of creation.
8. Print the last international competitor.
9. Print the major clothes colors in the US.
10. Print the amount of key value pairs (ie. length of the dictionary).
11. Print the keys of the dictionary.
12. Create another dictionary called more_on_zara with the following details:

creation_date: 1975 
number_stores: 10 000


13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
14. Print the value of the key number_stores. What just happened ?
"""

# 2
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

# 3
brand['number_stores'] = 2

# 4
print(f"Zara clients are {brand['type_of_clothes']} .")

# 5
brand['country_creation'] = 'Spain'

# 6
print(brand.keys())
if 'international_competitors' in brand.keys():
    brand['international_competitors'] += ['Desigual']

# 7
del brand['creation_date']

# 8
print(brand['international_competitors'][-1])

# 9
print(brand['major_color']['US'])

# 10
print(len(brand))

# 11
print(brand.keys())

# 12
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

# 13
brand.update(more_on_zara)

# 14
print(brand['number_stores'])
# When updating the dict brand with data from dict more_on_zara,
# the value associated to key 'number_stores' was updated from 2 to 10000 (value found on dict more_on_zara)


"""
Exercise 4 : Disney Characters
Instructions
Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
Analyse these results :

#1/

>>> print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/

>>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ 

>>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
Only recreate the 1st result for:
The characters, which names contain the letter “i”.
The characters, which names start with the letter “m” or “p”.
"""

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
users_sort = users.copy()
users_sort.sort()
users_len = len(users)

# 1 > print(disney_users_A)
usersA = {}
n = 0

for key in users:
    usersA[key] = n
    n += 1
print(usersA)

# 2 > print(disney_users_B)
usersB = {}
n = 0

for n in range(0, users_len, 1):
    usersB[n] = users[n]
    n += 1

print(usersB)


# 3 > print(disney_users_C)
# Using method sort()

# 3 > print(disney_users_C)

usersC = {}
n = 0

for key in users_sort:
    usersC[key] = n
    n += 1
print(usersC)

# 4
# Didn't really understand what is expected


# 5
# Didn't really understand what is expected
