
print("\n--- Mini-project: Anagram Checker ---\n")

import os
from itertools import permutations
dir_path = os.path.dirname(os.path.realpath(__file__))

# Item 1

class AnagramChecker:

# Item 2

    def __init__(self,file_name):
        self.file_name = file_name
        with open(dir_path + f'\\{file_name}', 'r') as file_obj:
            self.file_string = file_obj.read()
        self.file_list = self.file_string.lower().split()

    def is_valid_word(self,word):
        return word.lower() in self.file_list

    def anagrams(self,word):
        perm = permutations(word)
        list_tupples = list(perm)
        anagrams_qty = len(list_tupples)
        anagrams = []
        for i in range(anagrams_qty):
            if ("".join(list_tupples[i])) in self.file_list and ("".join(list_tupples[i])) != word:
                anagrams.append("".join(list_tupples[i]))
        return anagrams


testing = AnagramChecker('sowpods.txt')



