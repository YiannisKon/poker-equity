
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

print(Card("King", "hearts") == Card("King", "hearts"))   # want True
print(Card("King", "hearts") == Card("King", "spades"))   # want False
print(Card("Queen", "hearts") == Card("King", "hearts"))  # want False
print(Card("King", "hearts") == "banana")
print(Card("King", "hearts") == 5)
print(Card("King", "hearts"))
        
