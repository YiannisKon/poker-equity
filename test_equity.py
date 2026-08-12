from equity import parse_hand, simulate
from cards import Card


def test_parse_hand():
    hand = parse_hand("AhKh")
    assert hand == [Card("Ace", "hearts"), Card("King", "hearts")]


def test_parse_hand_ten():
    hand = parse_hand("Th2s")
    assert hand[0].rank == 10


def test_aa_beats_kk():
    aa = [Card("Ace", "hearts"), Card("Ace", "spades")]
    kk = [Card("King", "hearts"), Card("King", "spades")]
    eq1, eq2 = simulate(aa, kk)
    assert 79 < eq1 < 83
    assert eq1 + eq2 == 100