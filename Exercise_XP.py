"""
Exercise 1 : Set
Instructions
Create a set called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
"""

my_fav_numbers = {7,10,17,21,27}
print(my_fav_numbers)
my_fav_numbers.add(33)
my_fav_numbers.add(35)
print(my_fav_numbers)
set_len = len(my_fav_numbers)
my_fav_numbers.discard(set_len-1)
print(my_fav_numbers)
list_of_set = list(my_fav_numbers)
result_list = list_of_set[:-1]
print(result_list)
my_fav_numbers = set(result_list)
print("my_fav_numbers:", my_fav_numbers)

friend_fav_numbers = {4,7,15,21,27,30}
print("friend_fav_numbers:", friend_fav_numbers)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("our_fav_numbers:", our_fav_numbers)



"""
Exercise 2: Tuple
Instructions
Given a tuple which value is integers, is it possible to add more integers to the tuple?
"""

# No. Once the tuple is created it IS NOT possible to add new elements to it.



"""
Exercise 3: List
Instructions
Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)
"""

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.pop(basket.index("Banana"))
basket.pop(basket.index("Blueberries"))
basket.insert(len(basket), "Kiwi")
basket.insert(0,"Apples")
basket.count("Apples")
basket.clear()
print(basket)



"""
Exercise 4: Floats
Instructions
Recap – What is a float? What is the difference between an integer and a float?
Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
Can you think of another way to generate a sequence of floats?
"""

# Float is a data type used for numbers. The difference between float and integer is that float accepts decimals.

my_list = list()
for i in range(3,11,1):
    if i%2 == 0:
        my_list.append(int(i/2))
    else:
        my_list.append(i / 2)

print(my_list)

# It is possible to generate a sequence of floats by adding a float (can be 0.0) to a sequence of integers



"""
Exercise 5: For Loop
Instructions
Use a for loop to print all numbers from 1 to 20, inclusive.
Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
"""

for i in range(0,20,1):
    print(i+1)

for i in range(0,20,1):
    if i % 2 == 0:
        print(i+1)



"""
Exercise 6 : While Loop
Instructions
Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
"""

my_name = "Shlomo"
name = ""
while name != my_name:
    name = input("What is your name? ")



"""
Exercise 7: Favorite Fruits
Instructions
Ask the user to input their favorite fruit(s) (one or several fruits).
Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
Store the favorite fruit(s) in a list (convert the string of words into a list of words).
Now that we have a list of fruits, ask the user to input a name of any fruit.
If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
"""

fruits = input("Enter a your favorite fruit(s) separated by a single space: ")
fruits_list = fruits.split()
select_fruit = input("Enter a name of any fruit: ")
if select_fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit! I hope you enjoy")



"""
Exercise 8: Who Ordered A Pizza ?
Instructions
Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
"""

toppings = list()

while True:
    topping = input("What topping do you want to order? Enter 'quit' when you are done.\n>")
    if topping == "quit":
        break
    else:
        toppings.append(topping)
        print(f"A new topping was successfully added to your pizza: {topping}")

num_toppings = len(toppings)
price = 10 + 2.5 * num_toppings
print(f"Toppings selected:  {toppings} . The final price is {price}.")



"""
Exercise 9: Cinemax
Instructions
A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Ask a family the age of each person who wants a ticket.

Store the total cost of all the family’s tickets and print it out.

A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list.
"""

ages = input("Add the ages of family members separated by a single space: ")
ages_list = ages.split()
ages_int_list =[int(x) for x in ages_list]

cost = 0

for i in ages_int_list:
    if i > 12:
        cost += 15
    elif i >= 3:
        cost += 10

print(f"The cost for all the family members is: {cost}")

# Second part

teenagers_list = ["John", "Smith", "Jane", "Maria", "Carlos", "Talia", "Gal"]

teenagers_approved = list()
for i in teenagers_list:
    current_age = int(input(f"{i}, what is your age? "))
    if current_age >= 16 and current_age <= 21:
        teenagers_approved.append(i)

print(f"Teenagers approved to watch the movie: {teenagers_approved} .")



"""
Exercise 10 : Sandwich Orders
Instructions
Using the list below :

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
We need to prepare the orders of the clients:
Create an empty list called finished_sandwiches.
One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
I made your tuna sandwich
I made your avocado sandwich
I made your egg sandwich
I made your chicken sandwich
"""

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
num_orders = len(sandwich_orders)
pastrami_orders = sandwich_orders.count("Pastrami sandwich")
pastrami_excluded = 0
a = 1

while pastrami_excluded < pastrami_orders:
    if sandwich_orders[num_orders-a] == "Pastrami sandwich":
        sandwich_orders.pop(num_orders-a)
        pastrami_excluded += 1
    a +=1

finished_sandwiches = list()

num_orders = len(sandwich_orders)
transferred_items = 0

while transferred_items < num_orders:
    finished_sandwiches.append(sandwich_orders[0])
    transferred_items += 1
    sandwich_orders.pop(0)

for s in finished_sandwiches:
    print(f"I made your {s}")