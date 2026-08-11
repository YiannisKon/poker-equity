from cards import Card
from evaluator import is_flush, is_straight, evaluate_hand


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


def test_hand_evaluator():
    straight_flush = [Card("10", "hearts"), Card("9", "hearts"), Card("8", "hearts"), 
                  Card("7", "hearts"), Card("6", "hearts")]
    
    four_of_a_kind = [Card("10", "hearts"), Card("10", "spades"), Card("10", "clubs"), 
                  Card("7", "hearts"), Card("10", "diamonds")]
    
    full_house = [Card("9", "hearts"), Card("9", "clubs"), Card("9", "spades"), 
                  Card("King", "diamonds"), Card("King", "hearts")]

    flush = [Card("King", "hearts"), Card("9", "hearts"), Card("8", "hearts"), 
                  Card("3", "hearts"), Card("Queen", "hearts")]

    straight = [Card("10", "clubs"), Card("9", "hearts"), Card("8", "hearts"), 
                  Card("7", "hearts"), Card("6", "spades")]

    three_of_a_kind = [Card("9", "hearts"), Card("9", "spades"), Card("8", "hearts"), 
                  Card("7", "hearts"), Card("9", "clubs")]
    
    two_pair = [Card("Ace", "hearts"), Card("Ace", "clubs"), Card("2", "spades"), 
                  Card("2", "diamonds"), Card("King", "hearts")] 

    one_pair = [Card("King", "hearts"), Card("King", "diamonds"), Card("8", "hearts"), 
                  Card("7", "hearts"), Card("2", "spades")]

    high_card = [Card("Ace", "spades"), Card("7", "clubs"), Card("3", "hearts"), 
                  Card("4", "diamonds"), Card("9", "hearts")]  
    
    wheel_sf = [Card("Ace", "hearts"), Card("2", "hearts"), Card("3", "hearts"), 
                  Card("4", "hearts"), Card("5", "hearts")]

    assert evaluate_hand(straight_flush)  ==    (9, 10)
    assert evaluate_hand(four_of_a_kind)  ==    (8, 10, 7)
    assert evaluate_hand(full_house)      ==    (7, 9, 13)
    assert evaluate_hand(flush)           ==    (6, 13, 12, 9, 8, 3)
    assert evaluate_hand(straight)        ==    (5, 10)
    assert evaluate_hand(three_of_a_kind) ==    (4, 9, 8, 7)
    assert evaluate_hand(two_pair)        ==    (3, 14, 2, 13)
    assert evaluate_hand(one_pair)        ==    (2, 13, 8, 7, 2)
    assert evaluate_hand(high_card)       ==    (1, 14, 9, 7, 4, 3)
    assert evaluate_hand(wheel_sf)        ==    (9, 5)
