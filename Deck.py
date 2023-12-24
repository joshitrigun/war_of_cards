from Card import *


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create the Card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


new_deck = Deck()
new_deck.shuffle()
new_deck.deal_one()
# print(new_deck.all_cards[-1])

# for card_object in new_deck.all_cards:
#     print(card_object)

print(len(new_deck.all_cards))