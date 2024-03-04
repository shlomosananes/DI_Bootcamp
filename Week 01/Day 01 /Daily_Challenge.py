"""
1- Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.
If it’s 10 characters, print a message which states “perfect string” and continue the exercise.
"""

string_len = 0
while string_len != 10:
    string = input("Enter a string: ")
    string_len = len(string)
    if string_len < 10:
        print("string not long enough")
    elif string_len > 10:
        print("string too long")
    else:
        print("perfect string")



"""
2- Then, print the first and last characters of the given text.
"""

i = 0
while i < 10:
    if i == 0 or i == 9:
        print(string[i])
    i += 1



"""
3- Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
The user enters "HelloWorld"
Then, you have to construct the string character by character
H
He
Hel
... etc
HelloWorld
"""

for i in range (0,10,1):
    print(string[i])



"""
4- Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
"""

characters = [string[0],string[1],string[2],string[3],string[4],string[5],string[6],string[7],string[8],string[9]]
import random
random.shuffle(characters)
print(characters[0]+characters[1]+characters[2]+characters[3]+characters[4]+characters[5]+characters[6]+characters[7]+characters[8]+characters[9])

