# Include Card and Deck classes from the last two exercises.
# Deck of Cards
import random 
class Card:
    CARD_RANKS = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    @property
    def value(self):
        return Card.CARD_RANKS.get(self.rank, self.rank)
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._get_new_deck()

    def _get_new_deck(self):
        self._deck = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]
        random.shuffle(self._deck)

    def draw(self):
        if not self._deck:
            self._get_new_deck()
        return self._deck.pop()


class PokerHand:
    def __init__(self, deck):
        self._hand = [deck.draw() for _ in range(5)]

    def print(self):
        for card in self._hand:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        lowest_rank = 10
        for card in self._hand:
            if card.value < lowest_rank:
                lowest_rank = card.value
            
        return self._is_straight_flush() and lowest_rank == 10


    def _is_straight_flush(self):
        return self._is_straight() and self._is_flush()

    def _is_four_of_a_kind(self):
        return self.__n_of_a_kind(4)

    def _is_full_house(self):
        return (self._is_three_of_a_kind() and
                self._is_pair())

    def _is_flush(self):
        return all([card.suit == self._hand[0].suit for card in self._hand])

    def _is_straight(self):
        values = sorted([card.value for card in self._hand])
        sequence = list(range(values[0], values[0] + 5))
        return values == sequence

    def _is_three_of_a_kind(self):
        return self.__n_of_a_kind(3)

    def _is_two_pair(self):
        card_count = {}
        for card in self._hand:
            card_count[card.value] = card_count.get(card.value, 0) + 1
        
        matches = [1 for count in card_count.values() if count == 2]

        return len(matches) == 2

    def _is_pair(self):
        return self.__n_of_a_kind(2)

    def __n_of_a_kind(self, num):
        card_count = {}
        for card in self._hand:
            card_count[card.value] = card_count.get(card.value, 0) + 1
        
        matches = [1 for count in card_count.values() if count == num]
        return len(matches) == 1


hand = PokerHand(Deck())
hand.print()
# print(hand.evaluate())
print()

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards


hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")