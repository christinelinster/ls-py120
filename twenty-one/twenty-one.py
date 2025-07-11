import random
import os

def clear_screen():
    os.system("clear")

class Card:
    CARD_RANKS = {'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        if self.rank in Card.CARD_RANKS:
            return Card.CARD_RANKS[self.rank]
        return int(self.rank)

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
    BUST_VALUE = 21
    def __init__(self):
        self.hand = []

    def hit(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        total = 0 
        aces = 0
        for card in self.hand:
            if card.rank == "Ace":
                aces += 1
            else: 
                total += card.value()

        for _ in range(aces):
            if total + 11 < 21:
                total += 11
            else:
                total += 1
        return total
    
    def is_busted(self):
        if self.get_hand_value() > Participant.BUST_VALUE:
            return True
        return False
    
    def __str__(self):
        return self.__class__.__name__


class Player(Participant):
    def __init__(self):
        super().__init__()
        self.balance = 5

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self._reveal = False

    @property
    def reveal(self):
        return self._reveal
    
    @reveal.setter
    def reveal(self, reveal):
        self._reveal = reveal


class TwentyOneGame:
    NO_DEALER_HIT = 17
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()

    def start(self):
        self.display_welcome_message()
        self.deal_cards()

        self.show_cards()
        self.show_dealer_cards()

        self.play_turn()
        self.dealer.reveal = True

        if self.player.is_busted():
            self.display_result()
        else:
            self.dealer_turn()
            self.display_result()

        
        self.display_goodbye_message()

    def deal_cards(self):
        for _ in range(2):
            self.player.hit(self.deck.deal())
            self.dealer.hit(self.deck.deal())

    def show_cards(self):
        print("Your cards are: ")
        for card in self.player.hand:
            print(f"==> {card}")
        print()

    def show_dealer_cards(self):
        print(f"The dealer's cards are: ")
        cards = self.dealer.hand

        if not self.dealer.reveal:
            cards = cards[1:]
            print("==> ?")
        
        for card in cards:
                print(f"==> {card}")
        print()


    def show_value(self, participant):
        print(f"{participant} total value: {participant.get_hand_value()}")


    def play_turn(self):
        while True:
            self.show_value(self.player)
            prompt = "Hit or stay? (h/s): "
            choice = input(prompt).lower()

            if choice.startswith("h"):
                print("You chose to hit!")
                card = self.deck.deal()
                self.player.hit(card)

                if self.player.is_busted():
                    break

            elif choice.startswith("s"):
                print("You decided to stay.")
                break
            else:
                print("That's not a valid choice.\n")

    def dealer_turn(self):
        while True: 
            if self.dealer.get_hand_value() < TwentyOneGame.NO_DEALER_HIT:
                card = self.deck.deal()
                self.dealer.hit(card)
            else:
                break
            
            if self.dealer.is_busted():
                break

    def display_welcome_message(self):
        print("Welcome to the Twenty One Game!\n")

    def display_goodbye_message(self):
        print("\nThank you for playing the Twenty One Game. Goodbye!")

    def display_result(self):
        if self.player.is_busted():
            print("\nYou busted! You lose!")
        elif self.dealer.is_busted():
            print("\nDealer busted! You win!")
        else:
            dealer_value = self.dealer.get_hand_value()
            player_value = self.player.get_hand_value()
            if dealer_value > player_value:
                print("\nDealer wins!")
            elif player_value > dealer_value:
                print("\nYou win!")
            else:
                print("\nTie game!")
        
        self.show_value(self.player)
        self.show_cards()

        self.show_value(self.dealer)
        self.show_dealer_cards()
        

game = TwentyOneGame()
game.start()