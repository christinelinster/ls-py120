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

    def get_new_deck(self):
        self._deck = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]
        random.shuffle(self._deck)

    def deal(self):
        if not self._deck:
            self.get_new_deck()
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
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
        return total
    
    def is_busted(self):
        return self.get_hand_value() > Participant.BUST_VALUE
    
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
    MIN_BALANCE = 1
    MAX_BALANCE = 9
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()

    def start(self):
        clear_screen()
        self.display_welcome_message()
        self.display_player_balance()
        
        while not self.is_game_over():
            self.play_one_round()
            self.display_player_balance()
            if not self.play_again():
                break
            clear_screen()
            self.reset_game()

        if self.is_game_over():
            self.display_game_over_message()

        self.display_goodbye_message()

    def play_one_round(self):
        self.deal_cards()
        self.show_cards()
        self.show_dealer_cards()

        self.play_turn()
        self.dealer.reveal = True

        if not self.player.is_busted():
            self.dealer_turn()
        
        self.display_result()
        self.update_player_balance()

    def is_game_over(self):
        if TwentyOneGame.MIN_BALANCE <= self.get_player_balance() <= TwentyOneGame.MAX_BALANCE:
            return False
        return True
    
    def display_game_over_message(self):
        if self.get_player_balance() < TwentyOneGame.MIN_BALANCE:
            print("Sorry, you're broke!")
        elif self.get_player_balance > TwentyOneGame.MAX_BALANCE:
            print("You're too rich!")
        
    def play_again(self):
        while True:
            answer = input(f"Do you want to play again?(y/n): ").lower()
            if answer in ("y", "yes", "n", "no"):
                break
            print("Please enter a valid input.")

        return answer.startswith("y")

    def reset_game(self):
        self.player.hand = []
        self.dealer.hand = []
        self.dealer.reveal = False
        
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
            clear_screen()

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
        input("Press enter when you're ready for the dealer: ")
        while True: 
            if self.dealer.get_hand_value() >= TwentyOneGame.NO_DEALER_HIT or self.dealer.is_busted():
                break
            else:
                card = self.deck.deal()
                self.dealer.hit(card)

    def display_welcome_message(self):
        print("Welcome to the Twenty One Game!\n")

    def display_goodbye_message(self):
        print("\nThank you for playing the Twenty One Game. Goodbye!")

    GAME_RESULTS = {"Dealer": "Dealer wins!", "Player": "Player wins!", "Tie": "Tie game!"}
    
    def get_winner(self):
        dealer_value = self.dealer.get_hand_value()
        player_value = self.player.get_hand_value()

        if self.dealer.is_busted():
            return "Player"
        elif self.player.is_busted():
            return "Dealer"
        else:
            if dealer_value > player_value:
                return "Dealer"
            elif player_value > dealer_value:
                return "Player"
            else:
                return "Tie"
        
    def display_player_balance(self):
        print(f"Your current balance is: {self.get_player_balance()}")

    def update_player_balance(self):
        if self.get_winner() == "Dealer":
            self.player.balance -= 1
        elif self.get_winner() == "Player":
            self.player.balance += 1

    def get_player_balance(self):
        return self.player.balance

    def display_result(self):
        clear_screen()
        if self.player.is_busted():
            print("You busted! You lose!\n")
        elif self.dealer.is_busted():
            print("Dealer busted! You win!\n")
        else:
            winner = self.get_winner()
            print(f"{self.GAME_RESULTS[winner]}\n")

        self.show_value(self.player)
        self.show_cards()

        self.show_value(self.dealer)
        self.show_dealer_cards()
        

game = TwentyOneGame()
game.start()