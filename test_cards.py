from cards import Deck

def test_number_of_cards_initially():
    d = Deck()
    assert len(d.cards) == 52

def test_all_cards_unique():
    d = Deck()
    assert len(set(d.cards)) == 52