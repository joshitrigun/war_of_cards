import random

suits = ("Clubs", "Diamonds", "Hearts", 'Spades')
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14

}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


two_of_hearts = Card("Hearts", "Two")
three_of_clubs = Card("Clubs", "Three")

# print(two_of_hearts)
# print(two_of_hearts.suit)
# print(two_of_hearts.rank)
# print(two_of_hearts.value)
#
#
# print(three_of_clubs)
# print(three_of_clubs.suit)
# print(three_of_clubs.rank)
# print(three_of_clubs.value)

# print(two_of_hearts.value == three_of_clubs.value)