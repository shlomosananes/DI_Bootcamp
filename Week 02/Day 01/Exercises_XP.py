print("\n--- Outputs of Exercise 1: Cats ---\n")

"""
Exercise 1: Cats
Instructions
Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
Instantiate three Cat objects using the code provided above.
Outside of the class, create a function that finds the oldest cat and returns the cat.
Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
"""

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Cat1", 5)
cat2 = Cat("Cat2", 7)
cat3 = Cat("Cat3", 9)

# ## Tentando nao hard-code >> Isso nao funciona pois o resultado da expressao longa nao eh uma lista simples
# cats_list = [obj for obj in globals().values() if isinstance(obj,Cat)]
# print(cats_list)
#
# ## Se definirmos um atributo da lista, ai sim passa a ser simples e possivel de escrever uma lista
# cats_names_list = [obj.name for obj in globals().values() if isinstance(obj,Cat)]
# print(cats_names_list)


def find_oldest_cast():
    cats_age = [cat1.age, cat2.age, cat3.age]
    cats_name = [cat1.name, cat2.name, cat3.name]
    merging = list(zip(cats_age, cats_name))
    merging.sort(key=lambda x: x[0], reverse=True)
    print(f"The oldest cat is {merging[0][1]} and it is {merging[0][0]} years old.")

find_oldest_cast()




print("\n--- Outputs of Exercise 2: Dogs ---\n")

"""
Exercise 2 : Dogs
Instructions
Create a class called Dog.
In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
Create a method called bark that prints the following string “<dog_name> goes woof!”.
Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
Print the details of his dog (ie. name and height) and call the methods bark and jump.
Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
Print the details of her dog (ie. name and height) and call the methods bark and jump.
Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
"""

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps " + str(self.height*2) + " cm high.")

davids_dog = Dog("Rex", 50)
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

def find_highest():
    dogs_list = [obj for obj in globals().values() if isinstance(obj,Dog)]
    dogs_names = []
    dogs_heights =[]

    for dog in dogs_list:
        dogs_names.append(dog.name)
        dogs_heights.append(dog.height)

    dogs_info = list(zip(dogs_names, dogs_heights))
    dogs_info.sort(key=lambda x: x[1], reverse=True)
    print(f"The biggest dog is {dogs_info[0][0]} and it is {dogs_info[0][1]} cm high!")

find_highest()

# Adding new dog
jackies_dog = Dog("Pini", 60)
print(f"{jackies_dog.name} was added.")

find_highest()





print("\n--- Outputs of Exercise 3: Who's the Song Producer ---\n")

"""
Exercise 3 : Who’s The Song Producer?
Instructions
Define a class called Song, it will show the lyrics of a song.
Its __init__() method should have two arguments: self and lyrics (a list).
Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
Create an object, for example:

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


Then, call the sing_me_a_song method. The output should be:

There’s a lady who's sure
all that glitters is gold
and she’s buying a stairway to heaven
"""

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()





print("\n--- Outputs of Exercise 4: Afternoon At The Zoo ---\n")

"""
Exercise 4 : Afternoon At The Zoo
Instructions
Create a class called Zoo.
In this class create a method __init__ that takes one parameter: zoo_name.
It instantiates two attributes: animals (an empty list) and name (name of the zoo).
Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
Create a method called get_animals that prints all the animals of the zoo.
Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
Example

{ 
    1: "Ape",
    2: ["Baboon", "Bear"],
    3: ['Cat', 'Cougar'],
    4: ['Eel', 'Emu']
}


Create a method called get_groups that prints the animal/animals inside each group.

Create an object called ramat_gan_safari and call all the methods.
Tip: The zookeeper is the one who will use this class.
Example
Which animal should we add to the zoo --> Giraffe
x.add_animal(Giraffe)
"""

#Item 1

class Zoo:

#Item 2
    def __init__(self, zoo_name, *animals):
        self.name = zoo_name
        self.animals = []

#Item 3
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

#Item 4
    def get_animals(self):
        print(self.animals)

#Item 5 - Remove item - Using method < remove() >
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

#Item 6 and 7 - Sort animals

    def sort_animals(self):

        self.animals.sort()
        first_letter = []

        for n in self.animals:
            if n[0] not in first_letter:
                first_letter.append(n[0])
        # print(self.animals)
        # print(first_letter)

        dictio = {}
        for i in range(1,len(first_letter)+1):
            dictio[i] = []
            for n in self.animals:
                if first_letter[i-1] == n[0]:
                    dictio[i].append(n)
        print(dictio)

ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Horse")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Horse")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Pig")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Pidgeot")

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Horse")
ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()



