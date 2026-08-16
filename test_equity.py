from cards import Card
from equity import parse_hand, simulate, simulate_vs_random
from pytest import approx

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
    assert eq1 + eq2 == approx(100)


def test_suited_vs_pair():
    AhKh = [Card("Ace", "hearts"), Card("King", "hearts")]
    QdQc = [Card("Queen", "diamonds"), Card("Queen", "clubs")]
    eq1, eq2 = simulate(AhKh, QdQc, 20_000)
    assert 44 < eq1 < 48
    assert eq1 + eq2 == approx(100)


def test_offsuit_vs_bottompair():
    AhKc = [Card("Ace", "hearts"), Card("King", "clubs")]
    _2d2c = [Card("2", "diamonds"), Card("2", "clubs")]
    eq1, eq2 = simulate(AhKc, _2d2c, 20_000)
    assert 45 < eq1 < 49
    assert eq1 + eq2 == approx(100)


def test_dominating_hand():
    AhAs = [Card("Ace", "hearts"), Card("Ace", "spades")]
    _7d2c = [Card("7", "diamonds"), Card("2", "clubs")]
    eq1, eq2 = simulate(AhAs, _7d2c, 20_000)
    assert 86 < eq1 < 90
    assert eq1 + eq2 == approx(100)


def test_mirror_hand():
    AhKh = [Card("Ace", "hearts"), Card("King", "hearts")]
    AdKd = [Card("Ace", "diamonds"), Card("King", "diamonds")]
    eq1, eq2 = simulate(AhKh, AdKd, 20_000)
    assert 48 < eq1 < 52
    assert eq1 + eq2 == approx(100)

def test_samesuits_hand():
    AhQh = [Card("Ace", "hearts"), Card("Queen", "hearts")]
    KhJh = [Card("King", "hearts"), Card("Jack", "hearts")]
    eq1, eq2 = simulate(AhQh, KhJh, 20_000)
    assert 61 < eq1 < 65
    assert eq1 + eq2 == approx(100)


def test_aces_vs_random_headsup():
    aces = [Card("Ace", "spades"), Card("Ace", "hearts")]
    eq = simulate_vs_random(aces, trials=20_000)
    assert 83 < eq < 87


def test_aces_vs_random_multiway():
    aces = [Card("Ace", "spades"), Card("Ace", "hearts")]
    eq = simulate_vs_random(aces, n_opponents=4, trials=20_000)
    assert 52 < eq < 59
    