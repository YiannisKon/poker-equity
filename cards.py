import random

rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
               "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
rank_names = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
              10: "10", 11: "Jack", 12: "Queen", 13: "King", 14: "Ace"} 

class Card:

    def __init__(self, rank: str, suit: str):
        self.rank = rank_values[rank]
        self.suit = suit

    def __repr__(self): 
        return f"{rank_names[self.rank]}({self.suit})"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))



suits = ["hearts", "diamonds", "clubs", "spades"]

class Deck:

    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in rank_values:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n: int):
        dealt = self.cards[:n]
        del self.cards[:n]
        return dealt

    def remove(self, cards):
        for c in cards:
            self.cards.remove(c)


            
if __name__ == "__main__":

    d = Deck()
    d.shuffle()
    print(d.deal(2))
    print(d.deal(2))
    print(d.deal(5))
    print(len(d.cards))

