"""
Challenge 1
Ask the user for a number and a length.
Create a program that prints a list of multiples of the number until the list length reaches length.
Examples
number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]
"""

numb = int(input("Please enter a number: "))
user_len = int(input("Please enter a length: "))

list_len = list()
for i in range(0,user_len,1):
    list_len.append((i+1)*numb)

print(list_len)



"""
Challenge 2
Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
Examples
user's word : "ppoeemm" ➞ "poem"
user's word : "wiiiinnnnd" ➞ "wind"
user's word : "ttiiitllleeee" ➞ "title"
user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
Notes
Final strings won’t include words with double letters (e.g. “passing”, “lottery”).
"""

string = input("Please enter a string: ")
string_len = len(string)
new_string = string[0]

i = 1
while i < string_len:
    if string[i] != string[i-1]:
        new_string += string[i]
    i += 1

print(new_string)
