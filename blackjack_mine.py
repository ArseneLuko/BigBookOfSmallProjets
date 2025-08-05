""" Blackjack by Lukáš Karásek after exploring code of same game from the book "Big book of small projects" by Al Sweigart. 
https://inventwithpython.com/bigbookpython/project4.html
Writen from scratch.
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
github: https://github.com/ArseneLuko
"""

import random
import sys

money = 5_000  # starting money
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.

def get_rank(hand):
    """ Count total rank.
    """
    sum_rank = 0
    num_of_aces = 0
    for _, rank in hand:
        if rank in ("K", "Q", "J"):
            sum_rank += 10
        elif rank == "A":
            sum_rank += 1
            num_of_aces += 1
        elif 2 <= rank <= 10:
            sum_rank += rank

    for _ in range(num_of_aces):
        if sum_rank + 10 <= 21:
            sum_rank += 10
    
    return sum_rank

def get_bet(maxBet):
    """ Get bet from player between 1 to actual money
    """
    print(f"Tvoje prostředky: {maxBet}")
    print(f"Kolik chceš vsadit? 1 - {maxBet} / (k) nebo (q) pro ukončení")

    # correct bet input loop
    while True:
        # bet = input("> ")    
        bet = '200'  # testing line 

        if bet.lower() in ("k", "q"):
            print("Děkuji za hru, hezký den.")
            sys.exit()

        if bet.isdecimal() and 1 < int(bet) <= maxBet:
            return int(bet)

        print(f"Musíš zadat celé číslo v rozmezí 1 až {maxBet}")

def get_deck():
    """ Generate a deck of 52 cards (2 to 10 and J, Q, K, A).
    The deck is save as a list of tuples (suit, rank)"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):  # through all suits
        for rank in range(2, 11):  # add cards with rank 2 to 10
            deck.append((suit, rank))
        for rank in ("J", "Q", "K", "A"):  # add cards "J", "Q", "K", "A"
            deck.append((suit, rank))
        
    random.shuffle(deck)
    return deck

def display_cards(player_hand, dealer_hand, hide_dealer_hand=True):
    """ Display cards of dealer and player and their sums, last attribute sets
    if the first card of dealer is hiden (true) or displayd (false).
    """

    player_rank = get_rank(player_hand)
    dealer_rank = get_rank(dealer_hand)

    # show or hide dealar rank and their firs card
    if hide_dealer_hand:
        print("Krupiér: *")
    else:
        print(f"Krupiér: {dealer_rank}")        
    draw_cards(dealer_hand, hide_dealer_hand)
    print(f"Hráč: {player_rank}")
    draw_cards(player_hand)

def draw_cards(hand, hide_dealre_hand=False):
    """Create 5 rows that shows all cards in hand
    """
    rows = ["","","","",""]  # prepared 5 rows for draw cards

    if hide_dealre_hand:
        rows[0] += " ___  "
        rows[1] += f"|{"?": <3}| "
        rows[2] += f"|{"*": ^3}| "
        rows[3] += f"|{"?": >3}| "
        rows[4] += " ¯¯¯  "

    for suit, rank in hand:
        rows[0] += " ___  "
        rows[1] += f"|{rank: <3}| "
        rows[2] += f"|{suit: ^3}| "
        rows[3] += f"|{rank: >3}| "
        rows[4] += " ¯¯¯  "

    for row in rows:
        print(row)

def main():
    # create empty hands, a deck, set initial values
    player_hand = []
    dealer_hand = []
    deck = get_deck()

    # main program loop
    while True: 
        print("""
             *** Blackjack *** \n
            Získejte 21 bodů, ale ne více.
            Karty Král, Královna a Kluk jsou za 10 bodů.
            Esa jsou za 1 nebo 11 bodů.
            Karty od 2 do 10 jsou za tolik bodů, kolik je jejich hodnota.
                (H)rát - vezme další kartu z balíku.
                (S)top - přestane přibírat karty z balíku.
                (D)vakrát větší sázku můžeš zvolit při prvním tahu,
                    ale můžeš přibrat už jen jednu kartu.
                (K)onec nebo (Q)uit - ukončí hru.
            V případě rovnosti bodů je hráči sázka vrácena.
            Krupiér přestane brát karty, když dosáhne 17 bodů.\n""") 
        bet = get_bet(money)
        print()
        print(f"Tvoje sázka: {bet}")
        print()
        
        # pick first 2 cards (if player hand is empty then both pick two cards)
        # to repair: now it works: dealer take, player taky, dealer take, player take -–> I want to work it like dealer take 2, player take 2
        if not len(player_hand):
            for _ in range(2):
                dealer_hand.append(deck.pop())
                player_hand.append(deck.pop())

        # display cards and hide dealers hand - last True argument
        display_cards(player_hand, dealer_hand, True)

        player_rank = get_rank(player_hand)
        dealer_rank = get_rank(dealer_hand)
        pass

        # TODO: jestli bude 

        break  # breaking main program loop 

    pass

if __name__ == "__main__":
    main()