"""
Instructions
Here is a python code that generate a list of 20000 random numbers, called list_of_numbers.
Extend this code to guess how many couples of numbers in list_of_numbers sum to target_number.

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728
"""

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728

count = 0

for i in range(20000):
    for j in range(i+1,20000):
        if list_of_numbers[i] + list_of_numbers[j] == target_number:
            count += 1
        j += 1
    i += 1

print(count)
