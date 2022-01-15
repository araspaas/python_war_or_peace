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

def test_can_pile_basic_turn():
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
    turn.pile_cards()
    assert turn.spoils == [card1, card3]

def test_can_pile_war_turn():
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
    player1 = Player('Calvin', deck1)
    player2 = Player('Hobbes', deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "war"
    turn.pile_cards()
    assert turn.spoils == [card1, card2, card5, card3, card4, card6]

def test_can_pile_MAD_turn():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Queen", 12)
    card4 = Card("spade", "7", 7)
    card5 = Card("diamond", "King", 13)
    card6 = Card("Spade", "King", 13)
    card7 = Card("Club", "10", 10)
    card8 = Card("Club", "Jack", 11)
    cards1 = [card1, card2, card5, card7]
    cards2 = [card3, card4, card6, card8]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player('Calvin', deck1)
    player2 = Player('Hobbes', deck2)
    turn = Turn(player1, player2)
    assert turn.type() == "MAD"
    turn.pile_cards()
    assert turn.spoils == []
    assert turn.player1.deck.cards == [card7]
    assert turn.player2.deck.cards == [card8]

def test_distributes_cards_to_winner_for_basic_turn():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    card4 = Card("spade", "7", 7)
    cards1 = [card1, card2]
    cards2 = [card3, card4]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player('Calvin', deck1)
    player2 = Player('Hobbes', deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "basic"
    assert turn.winner() == player2

    turn.pile_cards()
    turn.award_spoils(turn.winner())

    assert player2.deck.cards == [card4, card1, card3]
    assert player1.deck.cards == [card2]
    assert turn.spoils == []

def test_distributes_cards_to_winner_for_war_turn():
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
    player1 = Player('Calvin', deck1)
    player2 = Player('Hobbes', deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "war"
    assert turn.winner() == player2

    turn.pile_cards()
    turn.award_spoils(player2)

    assert player2.deck.cards == [card1, card2, card5, card3, card4, card6]
    assert player1.deck.cards == []
    assert turn.spoils == []
