# Part 1: Quizz

# What is a class?
# >> A class is a category of objects with same attributes/functions/methods
#
# What is an instance?
# >> An instance is one object that behaves according to the rules of its class
#
# What is encapsulation?
# >> Encapsulation is the action of making information inaccessible
#
# What is abstraction?
# >>
#
# What is inheritance?
# >> Inheritance is the property that instances of a child-class inherit rules/functions/methods from the parent-class
#
# What is multiple inheritance?
# >> Multiple inheritance is when one object is child of more than one parent-class.
# >> The attributes will be as for the first parent class declared but it will also be able to use methods from the other parent-classes declared
#
# What is polymorphism?
# >> Polymorphism refers to functions/methods that will execute a different action when applied to different objects or classes
#
# What is method resolution order or MRO?
# >> MRO is the order in which a methods are searched for in classes hierarchy.
# >> In other words, for an object in a child-class 'A' under a parent-class 'B',
# >> when calling a method 'X', python will look for a method 'X' defined for the child-class.
# >> If found, it will run the body of this method even if there is another method 'X' defined at the parent level.
#

import random

# Part 2: Create A Deck Of Cards Class.

class Card:

    def __init__(self):
        self.suit = ['Hearts','Diamonds','Clubs','Spades']
        self.value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards_combinations = []
        for suit in self.suit:
            for value in self.value:
                self.cards_combinations.append(f"{suit} - {value}")


class Deck:

    def __init__(self):
        self.cards = all_cards.cards_combinations.copy()


    def shuffle(self):
        if set(self.cards) == set(all_cards.cards_combinations):
            print("The deck is complete")
        else:
            self.cards = all_cards.cards_combinations.copy()
            random.shuffle(self.cards)
            print("\nThe deck was reset and randomly rearranged.")


    def deal(self):
        random.shuffle(self.cards)
        print(f"The card pulled is {self.cards.pop()}. It is now removed from the deck.")


all_cards = Card()
deck1 = Deck()


