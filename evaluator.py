from cards import Card, Deck 
from collections import Counter

def rank_counts(cards):
    ranks = []
    for c in cards:
        ranks.append(c.rank)
    return Counter(ranks)


def is_flush(cards):
    suits = set()
    ranks = []
    for c in cards:
        suits.add(c.suit)
        ranks.append(c.rank)
    if len(suits) == 1:
        return tuple(sorted(ranks, reverse= True))
    return None


def is_straight(cards):
    straight = []
    for c in cards:
        straight.append(c.rank)
    straight.sort()
    if straight == [2, 3, 4, 5, 14]:
        return 5
    for i in range(4):
        if straight[i + 1] - straight[i] != 1:
            return None
    return straight[4]

    



if __name__ == "__main__":
    hand = [Card("King", "hearts"),
            Card("King", "clubs"),
            Card("King", "spades"),
            Card("5", "diamonds"),
            Card("5", "hearts")
    ]
    print(rank_counts(hand))
    print(rank_counts(hand).most_common())