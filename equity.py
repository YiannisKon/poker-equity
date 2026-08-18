import argparse
from cards import Card, Deck
from evaluator import best_of_seven

RANKS_SHORT = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
                    "T": "10", "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}
    
SUITS_SHORT = {"h": "hearts", "d": "diamonds", "c": "clubs", "s": "spades"}


def simulate(hand_1, hand_2, board=None, trials=100_000):
    board = board or []
    wins_1 = 0
    wins_2 = 0
    ties = 0   
    hands = hand_1 + hand_2

    for _ in range(trials):
        deck = Deck()
        deck.remove(hands)
        deck.remove(board)
        deck.shuffle()
        full_board = board + deck.deal(5 - len(board))
        score_1 = best_of_seven(hand_1 + full_board)
        score_2 = best_of_seven(hand_2 + full_board)
        if score_1 > score_2:
            wins_1 += 1
        elif score_1 < score_2:
            wins_2 += 1
        else:
            ties += 1

    eq_1 = ((wins_1 + ties/2) / trials) * 100
    eq_2 = ((wins_2 + ties/2) / trials) * 100
    return (eq_1, eq_2)


def simulate_vs_random(hero_hand, board=None, n_opponents=1, trials=100_000):
    board = board or []
    hero_share = 0

    for _ in range(trials):
        deck = Deck()
        deck.remove(hero_hand)
        deck.remove(board)
        deck.shuffle()

        ops_hands = [deck.deal(2) for _ in range(n_opponents)]
        full_board = board + deck.deal(5 - len(board))

        hero_score = best_of_seven(hero_hand + full_board)
        ops_scores = [best_of_seven(hand + full_board) for hand in ops_hands]
        best_op = max(ops_scores)

        if hero_score > best_op:
            hero_share += 1
        elif hero_score == best_op:
            k = 1 + ops_scores.count(best_op)
            hero_share += 1/k

    return (hero_share / trials) * 100

        
def parse_hand(hand_str):
    if len(hand_str) == 4:
        rank_1, suit_1, rank_2, suit_2 = hand_str[0], hand_str[1], hand_str[2], hand_str[3]
        return [Card(RANKS_SHORT[rank_1], SUITS_SHORT[suit_1]), Card(RANKS_SHORT[rank_2], SUITS_SHORT[suit_2])]
    else: 
        raise ValueError("Invalid hand input! ")
    
def parse_board(board_str):
    if board_str is None:
        return []
    elif len(board_str) in (6, 8, 10):
        cards = []
        for i in range(0, len(board_str), 2):
            rank, suit = board_str[i], board_str[i+1]
            cards.append(Card(RANKS_SHORT[rank], SUITS_SHORT[suit]))
        return cards
    else:
        raise ValueError("Invalid Board input!")
    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Poker equity calculator")
    parser.add_argument("--hand_1", required=True, help="First hole hand, e.g. AhKh")
    parser.add_argument("--hand_2", help="Second hole hand, e.g. AhKh")
    parser.add_argument("--trials", type=int, default=100_000, help="Number of trials")
    parser.add_argument("--opponents", type=int, default=1, help="Number of opponents, e.g. 4")
    parser.add_argument("--board", default=None, help="Known Board cards e.g. Qh7c5d")
    args = parser.parse_args()

    hand_1 = parse_hand(args.hand_1)
    board = parse_board(args.board)
    hand_2 = parse_hand(args.hand_2) if args.hand_2 else None

    known = hand_1 + board + (hand_2 or [])
    if len(known) != len(set(known)):
        raise SystemExit("Duplicate in input! ")
    
    if hand_2:
        eq_1, eq_2 = simulate(hand_1, hand_2, board, args.trials)
        print(f"{eq_1:.1f}/{eq_2:.1f}")
    else:
        print(f"{simulate_vs_random(hand_1, board, args.opponents, args.trials):.1f}")