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

# Item 1

from Day02_Exercises_XP import Dog
import random

# Item 2 and Item 3

class PetDog(Dog):
    def __init__(self,name,age,weight,trained = False):
        super().__init__(name,age,weight)
        self.trained = trained

# Item 4

    def train(self):
        print(self.bark())
        if self.trained == True:
            self.trained = False
        else:
            self.trained = True

    def play(self, *dog_names):
        self.dog_names = dog_names
        valid_dogs = []
        valid_dogs.append(self.name)

        existing_dogs = [obj for obj in globals().values() if isinstance(obj,Dog)]

        for n in dog_names:
            if n in existing_dogs:
                valid_dogs.append(n.name)


        string = ",".join(valid_dogs) + " all play together!"
        print(string)

    def do_a_trick(self):
        trick = random.randint(0,3)
        tricks = {
            0 : "does a barrel roll" ,
            1 : "stands on his back legs" ,
            2 : "shakes your hand" ,
            3 : "plays dead"
        }
        print(f"{self.name} {tricks[trick]}")


pini = PetDog("Pini",10, 20,False)
toto = PetDog("Toto",8, 15,False)
rufo = PetDog("Rufo",6, 10,False)
titi = 2


pini.play(toto,rufo,titi)

pini.do_a_trick()





print("\n--- Exercise 4: Family ---\n")

"""
Exercise 4 : Family
Instructions
Create a class called Family and implement the following attributes:

members: list of dictionaries
last_name : (string)

Implement the following methods:

born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
family_presentation: a method that prints the family’s last name and all the members’ details.

Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

    [
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]
"""

class Family:

    def __init__(self, last_name, *members):
        self.last_name = last_name
        self.members = []

    def born(self, **information):
        self.information = information
        self.members.append(information)
        print(f"Congrats for the birth of baby {information['name']}!")

    def is_18(self,family_member):
        self.family_member = family_member
        age = 0
        for n in self.members:
            if family_member == n['name']:
                age = n['age']
        if age > 18:
            return True
        else:
            return False

    def family_presentation(self):
        print(f"\nThis is family {self.last_name}")
        fam_members = len(self.members)
        print("[")
        for i in range (0,fam_members-1):
            print(f"    {self.members[i]},")
        for i in range (fam_members-1,fam_members):
            print(f"    {self.members[i]}")
        print("]")

family1 = Family('Silva')

family1.born(name='Michael',age=35,gender='Male',is_child=False)
family1.born(name='Sarah',age=32,gender='Female',is_child=False)

family1.family_presentation()





print("\n--- Exercise 5: The Incredibles Family ---\n")

"""
Exercise 5 : TheIncredibles Family
Instructions
Create a class called TheIncredibles. This class should inherit from the Family class:
This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)

Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

Add a method called incredible_presentation which :

Print a sentence like “*Here is our powerful family **”
Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)

Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.

    [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ]

Call the incredible_presentation method.

Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.

Call the incredible_presentation method again.
"""

# Item 1
class TheIncredibles(Family):

    def __init__(self,last_name,*members):
        super().__init__(last_name, *members)

# Item 2
    def use_power(self, incredible_member):
        self.incredible_member = incredible_member
        age = 0
        for n in self.members:
            if n['name'] == self.incredible_member:
                age = n['age']
                if age < 18:
                    raise ValueError("The incredible member is not over 18 years old")
                else:
                    print(f"{n['name']}'s power is {n['power']}")

# Item 3
    def incredible_presentation(self):
        print("\n*Here is our powerful family**")
        super().family_presentation()

# Item 4

incredible_family_1 = TheIncredibles('Incredibles')
incredible_family_1.born(name='Michael',age=35,gender='Male',is_child=False, power='fly', incredible_name='MikeFly')
incredible_family_1.born(name='Sarah',age=32,gender='Female',is_child=False, power='read minds', incredible_name='SuperWoman')

# Item 5

incredible_family_1.incredible_presentation()

# Item 6

incredible_family_1.born(name='Jack',age=0,gender='Male',is_child=True, power='Unknown Power', incredible_name='SuperBaby')

# Item 7

incredible_family_1.incredible_presentation()

