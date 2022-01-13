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

def test_knows_basic_turn_type():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    card4 = Card("spade", "7", 7)
    cards1 = [card1, card2]
    cards2 = [card3, card4]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player("Van", deck1)
    player2 = Player("Kujo", deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "basic"

def test_knows_war_turn_type():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Queen", 12)
    card4 = Card("spade", "7", 7)
    card5 = Card("diamond", "King", 13)
    card6 = Card("diamond", "Ace", 14)
    cards1 = [card1, card2, card5]
    cards2 = [card3, card4, card6]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player("", deck1)
    player2 = Player("Kujo", deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "war"

def test_knows_MAD_turn_type():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Queen", 12)
    card4 = Card("spade", "7", 7)
    card5 = Card("diamond", "King", 13)
    card6 = Card("Spade", "King", 13)
    cards1 = [card1, card2, card5]
    cards2 = [card3, card4, card6]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player("Van", deck1)
    player2 = Player("Kujo", deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "MAD"

def test_knows_winner_of_basic_turn():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    card4 = Card("spade", "7", 7)
    cards1 = [card1, card2]
    cards2 = [card3, card4]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player("Van", deck1)
    player2 = Player("Kujo", deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "basic"
    assert turn.winner() == player2

def test_knows_winner_of_war_turn():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Queen", 12)
    card4 = Card("spade", "7", 7)
    card5 = Card("diamond", "King", 13)
    card6 = Card("diamond", "Ace", 14)
    cards1 = [card1, card2, card5]
    cards2 = [card3, card4, card6]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player("Van", deck1)
    player2 = Player("Kujo", deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "war"
    assert turn.winner() == player2

def test_knows_MAD_turn_winner():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Queen", 12)
    card4 = Card("spade", "7", 7)
    card5 = Card("diamond", "King", 13)
    card6 = Card("Spade", "King", 13)
    cards1 = [card1, card2, card5]
    cards2 = [card3, card4, card6]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player("Van", deck1)
    player2 = Player("Kujo", deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "MAD"
    assert turn.winner() == "No Winner"
