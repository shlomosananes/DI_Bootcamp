"""
Challenge 1 : Sorting
Instructions
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Use List Comprehension
Example:
Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world
"""

words = input("Enter a sequence of words separated by comma: ")
words_list = words.split(",")
words_list.sort()
result = ",".join(item for item in words_list)
print(result)





"""
Challenge 2 : Longest Word
Instructions
Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
Examples
longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"
longest_word("A thing of beauty is a joy forever.") ➞ "forever."
longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"
"""

words = input("Enter a sentence to get the longest word in it: ")
words_list = words.split()
num_words = len(words_list)

max0 = max ( map ( len , words_list) )

for item in range (num_words):
    if len(words_list[item]) == max0:
        longest = words_list[item]
        break
    else:
        item += 1

print(longest)






