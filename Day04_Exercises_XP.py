print("\n--- Exercise 1: Random Sentence Generator ---\n")

"""
Exercise 1 – Random Sentence Generator
Instructions
Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.
Hint : The generated sentences do not have to make sense.
Download this word list
Save it in your development directory.
Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?
Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
use the words list to get your random words.
the amount of words should be the value of the length parameter.
Take the random words and create a sentence (using a python method), the sentence should be lower case.
Create a function called main which will:
Print a message explaining what the program does.
Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
If the user inputs incorrect data, print an error message and end the program.
If the user inputs correct data, run your code.
"""

# Item 1 - Downloaded
# Item 2 - Saved

import os
import random
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

# Item 3 - Function get_words_from_file
# The correct data type to store the words is LIST

def get_words_from_file():
    with open(f"{dir_path}\\words_list.txt", 'r') as file_obj:
        lines_of_words = []
        for line in file_obj:
            lines_of_words.append((line).strip('\n'))
    return lines_of_words

# Items 4 and 5 - Create random sentences

def get_random_sentence(length):
    lines_of_words = get_words_from_file()
    random_end = len(lines_of_words)
    words_for_sentence = []
    for i in range(length):
        words_for_sentence.append( lines_of_words[ random.randint(0,random_end) ].lower() )
    sentence = " ".join(words_for_sentence)
    print(sentence)

# Item 6 - Create a function called main

def main():
    print('\nThe program works according to the following procedure.\n 1) Opens a file and stores the words in a list.\n 2) Receives from the user a number of words to create a random sentence.\n 3) Pick the random words and create a sentence.\n')
    try:
        users_input = input('How many words do you want in your sentence? ')
        number = int(users_input)
        if number >= 2 and number <= 20:
            get_random_sentence(number)
        else:
            raise ValueError('You must input a numeral between 2 and 20.')
    except ValueError as e:
        print(f'{e}\nInput not accepted!')


print(get_words_from_file())
get_random_sentence(8)
main()





print("\n--- Exercise 2: Working with JSON ---\n")

#
# Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }
#
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.
#

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Item 1 - Access 'salary'

data = json.loads(sampleJson)    # Transforming the JSON- (string that seems like a dictionary)  'sampleJson' into a dictionary (not creating new file)
salary = data['company']['employee']['payable']['salary']

# Item 2 - Add a key called birth_date

data['company']['employee']['birth_date'] = '7-11-89'

# Item 3 - Save the dictionary as JSON to a file  >> Creating a file named 'dictionary_XP' based on dictionary 'data'

with open(dir_path + '\\dictionary_XP.json', 'w') as f_obj:  # name of the file will be dictionary_XP
    json.dump(data, f_obj)  # dumps would create a JSON-string (like we had before)
                            # This will create a JSON file presenting the whole dictionary in a single line
                            # In order to improve the visualization we could add more arguments (as we did in class)
                            # The syntax would be:
                            # json.dump(my_family, f_obj, indent = 2 , sort_keys = True)
                            # Attention to the arguments _indent_  &  _sort_keys_


