from cards import Card
from equity import simulate, simulate_vs_random, parse_hand, parse_board
from pytest import approx, raises


# ---------- parsers ----------

def test_parse_hand_valid():
    assert parse_hand("AhKh") == [Card("Ace", "hearts"), Card("King", "hearts")]

def test_parse_hand_ten():
    assert parse_hand("Th2s")[0].rank == 10

def test_parse_hand_invalid_length():
    with raises(ValueError):
        parse_hand("AhKhQs")

def test_parse_board_none():
    assert parse_board(None) == []

def test_parse_board_flop():
    assert parse_board("Qh7c2d") == [Card("Queen", "hearts"), Card("7", "clubs"), Card("2", "diamonds")]

def test_parse_board_invalid_length():
    with raises(ValueError):
        parse_board("Qh7")


# ---------- tests vs known equity ----------

def test_aa_beats_kk():
    eq1, eq2 = simulate(parse_hand("AhAs"), parse_hand("KhKs"), trials=20_000)
    assert 78.5 < eq1 < 83.5
    assert eq1 + eq2 == approx(100)

def test_suited_vs_pair():
    eq1, eq2 = simulate(parse_hand("AhKh"), parse_hand("QdQc"), trials=20_000)
    assert 44 < eq1 < 48
    assert eq1 + eq2 == approx(100)

def test_offsuit_vs_bottompair():
    eq1, eq2 = simulate(parse_hand("AhKc"), parse_hand("2d2c"), trials=20_000)
    assert 45 < eq1 < 49
    assert eq1 + eq2 == approx(100)

def test_dominating_hand():
    eq1, eq2 = simulate(parse_hand("AhAs"), parse_hand("7d2c"), trials=20_000)
    assert 86 < eq1 < 90
    assert eq1 + eq2 == approx(100)

def test_mirror_hand():
    eq1, eq2 = simulate(parse_hand("AhKh"), parse_hand("AdKd"), trials=20_000)
    assert 48 < eq1 < 52
    assert eq1 + eq2 == approx(100)

def test_samesuits_hand():
    eq1, eq2 = simulate(parse_hand("AhQh"), parse_hand("KhJh"), trials=20_000)
    assert 61 < eq1 < 65
    assert eq1 + eq2 == approx(100)


# ---------- tests vs random equity ----------
                              
def test_aces_vs_1_random():
    eq = simulate_vs_random(parse_hand("AsAh"), trials=20_000)
    assert 83 < eq < 87

def test_aces_vs_multiple_random():
    eq = simulate_vs_random(parse_hand("AsAh"), n_opponents=4, trials=20_000)
    assert 52 < eq < 58

def test_equity_in_valid_range():
    eq = simulate_vs_random(parse_hand("7h2c"), trials=5_000)
    assert 0 <= eq <= 100


# ---------- boards ----------

def test_board_set_vs_draws():
    hero = parse_hand("AhKh")
    opponent = parse_hand("QdQc")
    board = parse_board("Qh7h2c")
    eq1, eq2 = simulate(hero, opponent, board, trials=20_000)
    assert 22 < eq1 < 28

def test_river_is_100():
    hero = parse_hand("AhKh")
    board = parse_board("QhJhTh7d2s")
    eq = simulate_vs_random(hero, board, trials=2_000)
    assert eq == 100

def test_board_always_ties():
    hero = parse_hand("7c2d")
    opponent = parse_hand("7h2s")
    board = parse_board("AhKhQhJhTh")
    eq1, eq2 = simulate(hero, opponent, board, trials=2_000)
    assert eq1 == 50 and eq2 == 50

