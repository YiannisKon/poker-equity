from cards import Card
from evaluator import is_flush, is_straight


def test_flush_returns_sorted_ranks():
    hand = [Card("King", "hearts"),
            Card("Jack", "hearts"),
            Card("9", "hearts"),
            Card("7", "hearts"),
            Card("2", "hearts")
    ]

    assert is_flush(hand) == (13, 11, 9, 7, 2)


def test_straight_returns_high_card():
    hand = [Card("King", "hearts"),
            Card("Jack", "spades"),
            Card("Ace", "clubs"),
            Card("10", "hearts"),
            Card("Queen", "spades")
    ]

    assert is_straight(hand) == 14


def test_wheel_straight():
    hand = [Card("Ace", "hearts"),
            Card("2", "spades"),
            Card("3", "diamonds"),
            Card("4", "hearts"),
            Card("5", "clubs")
    ]

    assert is_straight(hand) == 5


def test_near_miss_is_not_straight():
    hand = [Card("5", "clubs"),
            Card("4", "hearts"),
            Card("3", "spades"),
            Card("7", "hearts"),
            Card("2", "diamonds")
    ]

    assert is_straight(hand) == None


def test_non_flush_returns_none():
    hand = [Card("King", "spades"),
            Card("Jack", "hearts"),
            Card("9", "hearts"),
            Card("7", "hearts"),
            Card("2", "hearts")
    ]

    assert is_flush(hand) == None




