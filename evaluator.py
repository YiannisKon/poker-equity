from collections import Counter
from itertools import combinations

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


# poker hands: high card, one pair, two pair, three of a king, straight, flush, full house,
# four of a king, straight flush


def evaluate_hand(cards):
    counts = rank_counts(cards)
    ordered = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)
    count_pattern = [] # e.g.  [3, 2],  [2, 2, 1]
    rank_tiebreaker = [] # e.g. [9, 12] for 9-9-9-Q-Q
    for rank, count in ordered:
        rank_tiebreaker.append(rank)
        count_pattern.append(count)

    flush = is_flush(cards)
    straight = is_straight(cards)

    # Straight Flush:
    if flush and straight:
        return (9, straight)
    # Four of a kind:
    elif count_pattern == [4, 1]:
        return (8, *rank_tiebreaker)
    # Full House:
    elif count_pattern == [3, 2]:
        return (7, *rank_tiebreaker)
    # Flush:
    elif flush:
        return (6, *flush)
    # Straight:
    elif straight:
        return (5, straight)
    # Three of a kind:
    elif count_pattern == [3, 1, 1]:
        return (4, *rank_tiebreaker)
    # Two Pairs:
    elif count_pattern == [2, 2, 1]:
        return (3, *rank_tiebreaker)
    # One Pair:
    elif count_pattern == [2, 1, 1, 1]:
        return (2, *rank_tiebreaker)
    # High Card:
    else:
        return (1, *rank_tiebreaker)


def best_of_seven(seven_cards):
    return evaluate_hand(max(combinations(seven_cards, 5), key=evaluate_hand))