print("\n--- First part ---\n")

"""
-----------
FIRST PART
-----------
Instructions : Old MacDonald’s Farm
Take a look at the following code and output:
File: market.py

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
Output

McDonald's farm

cow : 5
sheep : 2
goat : 12

    E-I-E-I-0!

Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:
Create a class called Farm. How should it be implemented?
Does the Farm class need an __init__ method? If so, what parameters should it take?
How many methods does the Farm class need?
Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
Test your code and make sure you get the same results as the example above.
Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

-----------
SECOND PART
-----------
Expand The Farm
Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheeps.”. The method should call the get_animal_types function to get a list of the animals.
Note : In English the plural form of the word “sheep” is sheep. But for the purpose of the exercise, let’s say that if there is more than 1 animal, an “s” should be added at the end of the word.
"""



# Item 1

class Farm:

# Item 2: The parameters should be 'name' and 'animal'.
# The parameters animal does not need to be declared when defining a new object.

    def __init__(self, name, *animal):
        self.name = name
        self.animal = []

# Item 3: The Farm class will have 2 methods: 'add_animal' and 'get_info'
# Item 4: The method 'add_animal' will have 2 parameters: 'animal_name' and 'qty'.
# The parameter qty has a default value = 1 that will be used every time the user does not enter a specif qty.
    def add_animal(self,animal_name, qty = 1):
        times = 0
        while times < qty:
            self.animal.append(animal_name)
            times += 1

    def get_info(self):
        farm_list = [obj.animal for obj in globals().values() if isinstance(obj, Farm)]
        farm_list = farm_list[0]

        animals_reduced = []
        for animal in farm_list:
            if animal not in animals_reduced:
                animals_reduced.append(animal)

        dictio = {}
        for animal in animals_reduced:
            dictio[animal] = farm_list.count(animal)

        print(f"{self.name}'s farm \n")

        for k, v in dictio.items():
            print(f"{k} : {v}")

        print("\n    E-I-E-I-O!")

    # Second part - Item 1
    def get_animal_types(self):
        farm_list = [obj.animal for obj in globals().values() if isinstance(obj, Farm)]
        farm_list = farm_list[0]

        animals_reduced = []
        for animal in farm_list:
            if animal not in animals_reduced:
                animals_reduced.append(animal)

        animals_reduced.sort()

        return animals_reduced

    # Second part - Item 2 (method will be called in the end of the code)
    def get_short_info(self):
        animals_for_string = self.get_animal_types()
        animals_types = len(animals_for_string)
        list_for_string = list()
        list_for_string.append(f"{self.name}'s farm has ")
        for i in range (0,animals_types-2):
            list_for_string.append(f"{animals_for_string[i]}s, ")
        for i in range(animals_types - 2, animals_types - 1):
            list_for_string.append(f"{animals_for_string[i]}s and ")
        for i in range(animals_types - 1, animals_types):
            list_for_string.append(f"{animals_for_string[i]}s.")
        string = "".join(list_for_string)
        print(string)

# Item 5: Testing the code

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()


print("\n--- Second part ---\n")

# Second part - Item 2 (calling):
macdonald.get_short_info()





