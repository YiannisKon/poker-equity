import argparse
from cards import Card, Deck
from evaluator import best_of_seven

RANKS_SHORT = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
                    "T": "10", "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}
    
SUITS_SHORT = {"h": "hearts", "d": "diamonds", "c": "clubs", "s": "spades"}


def simulate(hand_1, hand_2, trials=100_000):
    # hand1, hand2, lists of 2 Card objects each
    wins_1 = 0
    wins_2 = 0
    ties = 0   
    hands = hand_1 + hand_2

    for _ in range(trials):
        deck = Deck()
        deck.remove(hands)
        deck.shuffle()
        dealt = deck.deal(5)
        player_1 = hand_1 + dealt
        player_2 = hand_2 + dealt
        score_1 = best_of_seven(player_1)
        score_2 = best_of_seven(player_2)
        if score_1 > score_2:
            wins_1 += 1
        elif score_1 < score_2:
            wins_2 += 1
        else:
            ties += 1

    eq_1 = ((wins_1 + ties/2) / trials) * 100
    eq_2 = ((wins_2 + ties/2) / trials) * 100
    return (eq_1, eq_2)


def simulate_vs_random(hero_hand, n_opponents=1, trials=100_000):
    hero_share = 0

    for _ in range(trials):
        deck = Deck()
        deck.remove(hero_hand)
        deck.shuffle()

        ops_hands = []
        for _ in range(n_opponents):
            ops_hands.append(deck.deal(2))
        board = deck.deal(5)

        hero_score = best_of_seven(hero_hand + board)
        ops_scores = []
        for i in ops_hands:
            ops_scores.append(best_of_seven(i + board))
        best_op_score = max(ops_scores)

        if hero_score > best_op_score:
            hero_share += 1
        elif hero_score == best_op_score:
            k = 1 + ops_scores.count(best_op_score)
            hero_share += 1/k

    return (hero_share / trials) * 100

        
def parse_hand(hand_str):
    rank_1, suit_1, rank_2, suit_2 = hand_str[0], hand_str[1], hand_str[2], hand_str[3]
    return [Card(RANKS_SHORT[rank_1], SUITS_SHORT[suit_1]), Card(RANKS_SHORT[rank_2], SUITS_SHORT[suit_2])]



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Poker equity calculator")
    parser.add_argument("--hand_1", required=True, help="First hole hand, e.g. AhKh")
    parser.add_argument("--hand_2", help="Second hole hand, e.g. AhKh")
    parser.add_argument("--trials", type=int, default=100_000, help="Number of trials")
    parser.add_argument("--opponents", type=int, default=1, help="Number of opponents, e.g. 4")
    args = parser.parse_args()

    hand_1 = parse_hand(args.hand_1)
    if args.hand_2:
        hand_2 = parse_hand(args.hand_2)
        eq_1, eq_2 = simulate(hand_1, hand_2, args.trials)
        print(f"{eq_1:.1f}/{eq_2:.1f}")
    else:
        print(f"{simulate_vs_random(hand_1, args.opponents, args.trials):.1f}")