
"""
Exercise 1 : What Are You Learning ?
Instructions
Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
Call the function, and make sure the message displays correctly.
"""

def display_message():
    print("Hellow World! I am learning Python!")

display_message()





"""
Exercise 2: What’s Your Favorite Book ?
Instructions
Write a function called favorite_book() that accepts one parameter called title.
The function should print a message, such as "One of my favorite books is <title>".
For example: “One of my favorite books is Alice in Wonderland”
Call the function, make sure to include a book title as an argument when calling the function.
"""

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("The Lion King")





"""
Exercise 3 : Some Geography
Instructions
Write a function called describe_city() that accepts the name of a city and its country as parameters.
The function should print a simple sentence, such as "<city> is in <country>".
For example “Reykjavik is in Iceland”
Give the country parameter a default value.
Call your function.
"""

def describe_city(city,country = "US"):
    print(f"{city} is in {country}.")

describe_city("Belem","Brazil")





"""
Exercise 4 : Random
Instructions
Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
"""

import random
def check_number (number1):
    number2 = random.randint(1,100)
    if number1 == number2:
        print("Well done! The numbers match!")
    else:
        print(f"Oh no, you failed! You guessed {number1} and the correct number was {number2}.")

check_number (int(input("Enter a number: ")))





"""
Exercise 5 : Let’s Create Some Personalized Shirts !
Instructions
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
Call the function make_shirt().

Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
Make a large shirt with the default message
Make medium shirt with the default message
Make a shirt of any size with a different message.

Bonus: Call the function make_shirt() using keyword arguments.
"""

#1 and #2
def make_shirt(size,message):
    print(f"The size of the shirt is {size} and the message is {message}")

#3
make_shirt(size="S",message="I love Python")

#4
def make_shirt(size = 'L',message = 'I love Python'):
    print(f"The size of the shirt is {size} and the message is {message}")

#5
make_shirt('L')

#6
make_shirt('M')

#7
sizes = ['S','M','L']
size = sizes[random.randint(0,2)]
make_shirt(size,"I don't really love Python")

#8
make_shirt(message="I love keyword arguments", size="S")





"""
Exercise 6 : Magicians …
Instructions
Using this list of magician’s names

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

Create a function called show_magicians(), which prints the name of each magician in the list.
Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
Call the function make_great().
Call the function show_magicians() to see that the list has actually been modified.
"""

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

#1
def show_magicians(list):
    for f in list:
        print(f)

show_magicians(magician_names)

#2
def make_great(list):
    list_len = len(list)
    i = 0
    while i < list_len:
        list[i] = f"The Great {list[i]}"
        i += 1

#3
make_great(magician_names)

#4
show_magicians(magician_names)





"""
Exercise 7 : Temperature Advice
Instructions
Create a function called get_random_temp().
This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
Test your function to make sure it generates expected results.

Create a function called main().
Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
between 16 and 23
between 24 and 32
between 32 and 40

Change the get_random_temp() function:
Add a parameter to the function, named ‘season’.
Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
Now that we’ve changed get_random_temp(), let’s change the main() function:
Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
Use the season as an argument when calling get_random_temp().

Bonus: Give the temperature as a floating-point number instead of an integer.
Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
"""

#1
def get_random_temp():
    return random.randint(-10,40)

#2
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")

#3
messages = {
    0 : "Brrr, that’s freezing! Wear some extra layers today" ,
    16 : "Quite chilly! Don’t forget your coat" ,
    23 : "It's pleasant outside if you are not in the shade" ,
    32 : "Weather is great, enjoy your day!" ,
    40 : "Summer is here! Don't forget sunblock and drink a lot of water!"
}

def main2():
    temp = get_random_temp()
    for max_temp in messages:
        if temp <= max_temp:
            print(f"The temperature right now is {temp} degrees Celsius.")
            print(messages[max_temp])
            break
main2()






"""
Exercise 8 : Star Wars Quiz
Instructions
This project allows users to take a quiz to test their Star Wars knowledge.
The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

Here is an array of dictionaries, containing those questions and answers

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
Create a function that informs the user of his number of correct/incorrect answers.
Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
If he had more then 3 wrong answers, ask him to play again.
"""

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

#1
correct = 0 #Counting correct answers
incorrect = 0 #Counting incorrect answers
wrong = [] #List of wrong answers

numb_questions = len(data)
print(numb_questions)

pos = 0

while pos < numb_questions:
    answer = input(data[pos]["question"])
    if answer == data[pos]["answer"]:
        correct += 1
    else:
        incorrect += 1
        wrong.append(answer)
    pos += 1

print(correct)
print(incorrect)
print(wrong)

#2
def results():
    print(f"You gave {correct} correct answers and {incorrect} incorrect answers.")

results()
