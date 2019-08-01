import random
from Card import Card
from Deck import Deck
from Player import Player

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}
player_turn = True


def take_bet(player):
    while True:
        try:
            money_to_bet = int(input(f"ok {player.name} how much do you wanna bet?"))
        except ValueError:
            print("Enter a valid Number!")
            continue
        else:
            if money_to_bet > player.money:
                print(f"your bet {money_to_bet} is higher than your money {player.money} ")
                continue
            else:
                player.curr_bet = money_to_bet
                break


def hit(deck, player):
    player.add_card(deck.deal())
    player.adjust_ace()


def hit_or_stand(deck, player):
    global player_turn

    while True:
        x = input("do you want to hit or stand? H / S")
        if x.upper() == 'H':
            hit(deck, player)
        elif x.upper() == 'S':
            print(f" {player.name} stands now its the Dealer turn")
            player_turn = False
        else:
            print("Please enter H or S")
            continue
        break


def show_some(player, dealer):
    print("Dealer Cards: HIDDEN CARD, ", end='')
    print(dealer.hand_cards[1])
    print(f"{player.name} Cards: " + player.get_hand())


def show_all(player, dealer):
    print(f"{player.name} Cards: " + player.get_hand())
    print("Dealer Cards: " + dealer.get_hand())


def player_busts(player, dealer):
    print(f"{player.name} YOU LOST!!!")
    player.lose_money(player.curr_bet)
    dealer.win_money(player.curr_bet)


def player_wins(player, dealer):
    print(f"{player.name} YOU WON!!!")
    player.win_money(player.curr_bet)
    dealer.lose_money(player.curr_bet)


def dealer_busts(player, dealer):
    print("Dealer LOST!!!")
    player.win_money(player.curr_bet)
    dealer.lose_money(player.curr_bet)


def dealer_wins(player, dealer):
    print("Dealer WON!!!")
    player.lose_money(player.curr_bet)
    dealer.win_money(player.curr_bet)


def tie(player):
    print("ITS A TIE! NO ONE LOST MONEY!")
    player.curr_bet = 0


def main():
    print("Welcome to the Worst Blackjack Game that was developed by one that doesnt know how to play BlackJack at all")
    playing = True
    global player_turn
    player_turn = True
    my_deck = Deck(suits, ranks)
    my_deck.shuffle()
    curr_player = Player(suits, ranks, values, "Stav")
    curr_dealer = Player(suits, ranks, values, "dealer")

    while playing:
        curr_player.add_card(my_deck.deal())
        curr_player.add_card(my_deck.deal())
        curr_dealer.add_card(my_deck.deal())
        curr_dealer.add_card(my_deck.deal())

        take_bet(curr_player)
        show_some(curr_player, curr_dealer)
        while player_turn:

            hit_or_stand(my_deck, curr_player)
            show_some(curr_player, curr_dealer)
            # print(curr_player.hand_value)
            if curr_player.hand_value > 21:
                player_busts(curr_player, curr_dealer)
                break

        if curr_player.hand_value <= 21:

            while curr_dealer.hand_value < 17:
                hit(my_deck, curr_dealer)

            show_all(curr_player, curr_dealer)

            if curr_dealer.hand_value > 21:
                dealer_busts(curr_player, curr_dealer)
            elif curr_dealer.hand_value > curr_player.hand_value:
                dealer_wins(curr_player, curr_dealer)
            elif curr_dealer.hand_value < curr_player.hand_value:
                player_wins(curr_player, curr_dealer)
            else:
                tie(curr_player)

        print(f"{curr_player.name} has: " + str(curr_player.money) + " Money and Dealer has: " + str(
            curr_dealer.money) + " Money")

        new_game = input(("do you wanna play again? enter y/n"))
        if new_game.lower() == 'y':
            player_turn = True
            my_deck = Deck(suits, ranks)
            my_deck.shuffle()
            curr_player.hand_value = 0
            curr_player.num_aces = 0
            curr_player.hand_cards.clear()
            curr_dealer.hand_value = 0
            curr_dealer.num_aces = 0
            curr_dealer.hand_cards.clear()
        elif new_game.lower() == 'n':
            break


if __name__ == '__main__':
    main()
