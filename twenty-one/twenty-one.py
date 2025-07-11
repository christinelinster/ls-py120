import random
import os

def clear_screen():
    os.system("clear")

class Card:
    CARD_RANKS = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        return Card.CARD_RANKS.get(self.rank, self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    def __init__(self):
        self.get_new_deck()
        # STUB
        # What attributes does a deck need? A collection of 52 cards? 
        # Some data structure like list or dictionary might be required

    def get_new_deck(self):
        self._deck = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop()

class Participant:
    def __init__(self):
        self.hand = []
        # STUB
        # What attributes does a participant require? Score? Hand? Betting Balance? 
        # What else goes bere? all the redundant behaviours from Player and Dealer?
    
    def add_to_hand(self, card):
        self.hand.append(card)

class Player(Participant):
    def __init__(self):
        super().__init__()
        self.balance = 5
        # STUB
        # What additional attributes might a player need? 
        # Score? Hand? Amount of money available?


    def hit(self):
        #STUB
        pass

    def stay(self):
        # STUB
        pass

    def is_busted(self):
        # STUB
        pass

    def score(self):
        # STUB
        pass

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        # STUB
        # Very similar to Player; do we need this?

    def hit(self):
        # STUB
        pass

    def stay(self):
        # STUB
        pass

    def is_busted(self):
        # STUB
        pass

    def score(self):
        # STUB
        pass

    def hide(self):
        # STUB 
        pass

    def reveal(self):
        # STUB
        pass

    def deal(self):
        # STUB
        pass

class TwentyOneGame:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        # STUB
        # How to keep track of points? Should that be done in participants? 

    def start(self):
        # SPIKE
        self.display_welcome_message()
        self.deal_cards()
        self.show_cards()
        self.play_turn()
        self.dealer_turn()
        self.display_result()
        self.display_goodbye_message()

    def deal_cards(self):
        for _ in range(2):
            self.player.add_to_hand(self.deck.deal())
            self.dealer.add_to_hand(self.deck.deal())

    def show_cards(self):
        player_cards = [card for card in self.player.hand]
        print("\nYour cards are: ")
        for card in player_cards:
            print(card)

        dealer_cards = [card for card in self.dealer.hand]
        print("\nThe dealer's cards are: ")
        print("?")
        for card in dealer_cards[1:]:
            print(card)

    def play_turn(self):
        # STUB
        pass

    def dealer_turn(self):
        # STUB
        pass

    def display_welcome_message(self):
        print("Welcome to the Twenty One Game!")

    def display_goodbye_message(self):
        print("\nThank you for playing the Twenty One Game. Goodbye!")

    def display_result(self):
        # STUB
        pass

game = TwentyOneGame()
game.start()