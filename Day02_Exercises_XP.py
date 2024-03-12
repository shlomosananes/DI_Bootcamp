print("\n--- Exercise 1: Pets ---\n")

"""
Exercise 1 : Pets
Instructions
Using this code:

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


Create another cat breed named Siamese which inherits from the Cat class.
Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
Take all the cats for a walk, use the walk method.
"""

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Item 1 - Create another cat breed named Siamese.

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Preparation for Item 2 - Creating objects (cats).

miau = Bengal('Miau', 1)
miauu = Chartreux('Miauu', 2)
miauuu = Siamese('Miauuu', 3)

# Item 2 - Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.

all_cats = [obj for obj in globals().values() if isinstance(obj,Cat)]

#---------------------------------------------------------------------------------
# VALIDATION
#
# all_cats_names = [obj.name for obj in globals().values() if isinstance(obj,Cat)]
# print(all_cats)
# print(all_cats_names)
#---------------------------------------------------------------------------------

# Item 3 - Create a variable called sara_pets which value is an instance of the Pet class.

sara_pets = Pets(all_cats)

# Item 4 - Take all the cats for a walk, use the walk method.

sara_pets.walk()





print("\n--- Exercise 2: Dogs ---\n")

"""
Exercise 2 : Dogs
Instructions
Create a class called Dog with the following attributes name, age, weight.
Implement the following methods in the Dog class:
bark: returns a string which states: “<dog_name> is barking”.
run_speed: returns the dogs running speed (weight/age*10).
fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

Create 3 dogs and run them through your class.
"""

# Item 1 - Create a class called Dog
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

# Item 2 - Implement methods

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight/self.age*10

    def fight(self, other_dog):
        dog1 = self.run_speed() * self.weight
        dog2 = other_dog.run_speed() * other_dog.weight
        # -------------
        # VALIDATION
        #
        # print(f"dog1 strength: {dog1}")
        # print(f"dog2 strength: {dog2}")
        # -------------
        if dog1 > dog2:
            return f"{self.name} won the fight!"
        elif dog2 > dog1:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"

# Item 3 - Creating 3 dogs and running the program

toto = Dog('toto',5,40)
rex = Dog('rex',3,30)
rufo = Dog('rufo',4,40)

print(toto.bark())
print(toto.run_speed())
print(rex.bark())
print(rex.run_speed())
print(rufo.bark())
print(rufo.run_speed())

print(toto.fight(rex))
print(toto.fight(rufo))
print(rex.fight(toto))
print(rex.fight(rufo))
print(rufo.fight(toto))
print(rufo.fight(rex))





print("\n--- Exercise 3: Dogs Domesticated ---\n")

"""
Exercise 3 : Dogs Domesticated
Instructions
Create a new python file and import your Dog class from the previous exercise.
In the new python file, create a class named PetDog that inherits from Dog.
Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
Add the following methods:
train: prints the output of bark and switches the trained boolean to True

play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

do_a_trick: If the dog is trained the method should print one of the following sentences at random:
“dog_name does a barrel roll”.
“dog_name stands on his back legs”.
“dog_name shakes your hand”.
“dog_name plays dead”.
"""

