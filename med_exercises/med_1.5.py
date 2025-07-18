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

deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).