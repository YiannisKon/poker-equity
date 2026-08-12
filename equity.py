from cards import Card, Deck
from evaluator import best_of_seven


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

    hand_1_eq = ((wins_1 + ties/2) / trials) * 100
    hand_2_eq = ((wins_2 + ties/2) / trials) * 100
    return (hand_1_eq, hand_2_eq)

if __name__ == "__main__":

    print(simulate([Card("Ace", "hearts"), Card("Ace", "spades")], [Card("King", "diamonds"), Card("King", "clubs")]))
    print(simulate([Card("Ace", "hearts"), Card("King", "hearts")], [Card("Queen", "hearts"), Card("Queen", "clubs")]))
    print(simulate([Card("Ace", "hearts"), Card("King", "clubs")], [Card("2", "hearts"), Card("2", "clubs")]))