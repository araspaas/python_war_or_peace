import pytest
from lib.turn import *
from lib.player import *
from lib.deck import *
from lib.card import *

def test_ist_exists():
    card1 = Card("heart", "King", 13)
    card2 = Card("spade", "King", 13)
    card3 = Card("club", "King", 13)
    card4 = Card("diamond", "King", 13)
    cards = [card1, card2, card3]
    deck = Deck(cards)

    player1 = Player("Van", deck)
    player2 = Player("Kujo", deck)

    turn = Turn(player1, player2)

    assert turn.player1.name == "Van"
    assert turn.player2.name == "Kujo"
    assert turn.spoils == []
