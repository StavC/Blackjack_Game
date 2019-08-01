class Player:
    def __init__(self, suits, ranks, values, name):
        self.hand_cards = []
        self.hand_value = 0
        self.num_aces = 0
        self.suits = suits
        self.ranks = ranks
        self.values = values
        self.money = 100  # default starting money
        self.name = name
        self.curr_bet = 0

    def add_card(self, card):
        self.hand_cards.append(card)
        self.hand_value += self.values[card.rank]
        if card.rank == 'Ace':
            self.num_aces += 1

    def adjust_ace(self):
        while self.hand_value > 21 and self.num_aces:
            self.hand_value -= 10
            self.num_aces -= 1

    def win_money(self, money_won):
        self.money += money_won

    def lose_money(self, money_lost):
        self.money -= money_lost

    def get_hand(self):
        my_str = ""
        for card in self.hand_cards:
            my_str += str(card.getter()) + ", "
        return my_str[:-2]
