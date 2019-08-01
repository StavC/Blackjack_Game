from Card import Card
from random import shuffle


class Deck():

    def __init__(self, suits, ranks):
        self.list_of_cards = []
        self.suits = suits
        self.ranks = ranks
        for suit in suits:
            for rank in ranks:
                curr_card = Card(suit, rank)
                # print(curr_card)
                self.list_of_cards.append(curr_card)

    def __str__(self):
        curr_card_str = ""
        for card in self.list_of_cards:
            curr_card_str += card.getter() + " \n"
        return curr_card_str

    def shuffle(self):
        shuffle(self.list_of_cards)

    def deal(self):
        card_to_deal = self.list_of_cards.pop()
        return card_to_deal
