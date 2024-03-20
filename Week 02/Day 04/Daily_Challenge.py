
print("\n--- Exercise 1: Text Analysis ---\n")

import os
import string
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1

# Item 1
class Text:

    def __init__(self,string):
        self.string = string
        self.counter = []

# Item 2 > Bullet 1
    def word_frequency(self,word):
        exclude_punctuation = string.punctuation
        my_string = self.string.split()
        elements = len(my_string)
        for i in range (elements):
            my_string[i] = my_string[i].lower().strip(exclude_punctuation)
        count_word = my_string.count(word)
        if count_word == 0:
            print("\nNone")
        else:
            print(f"\nThe word '{word}' was found {count_word}x in the text!")

# Item 2 > Bullet 2
    def most_common(self):
        exclude_punctuation = string.punctuation
        my_string = self.string.split()
        elements = len(my_string)
        dif_elements = []
        for i in range(elements):
            my_string[i] = my_string[i].lower().strip(exclude_punctuation)
            if my_string[i].lower().strip(exclude_punctuation) not in dif_elements:
                dif_elements.append(my_string[i].lower().strip(exclude_punctuation))
        dif_elements.sort()
        different_words = len(dif_elements)
        count_words = []
        for i in range(different_words):
            count_words.append(my_string.count(dif_elements[i]))
        self.counter = list(zip(count_words,dif_elements))
        self.counter.sort(key=lambda x: x[0], reverse =True)
        max_count = self.counter[0][0]
        max_count_words = []
        for i in range(different_words):
            if self.counter[i][0] == max_count:
                max_count_words.append(self.counter[i][1])
        print(f"\nThe most common(s) word(s) in the text, with {max_count} appearances, is(are): {", ".join(max_count_words)}  .")
        # print(f"\nList of all the different words in the text:\n{dif_elements}")

# Item 2 > Bullet 3

    def unique_words(self):
        unique_words = []
        num = len(self.counter)
        for i in range (num):
            if self.counter[i][0] == 1:
                unique_words.append(self.counter[i])
        print(f"\nList of all the unique words in the text:\n{unique_words}")

# Part 2

    @classmethod
    def from_file(cls, file_name):
        with open(dir_path + f'\\{file_name}', 'r') as file_obj:
            file_string = file_obj.read()

        return cls(string=file_string)



part1 = Text('A good book would sometimes cost as much as a good house.')
part1.word_frequency('as')
part1.most_common()
part1.unique_words()


part2 = Text.from_file('the_stranger.txt')

part2.word_frequency('as')
part2.most_common()
part2.unique_words()


