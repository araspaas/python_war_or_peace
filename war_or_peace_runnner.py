from lib.turn import *
from lib.player import *
from lib.deck import *
from lib.card import *
from lib.game import *

suits = ["Heart", "Diamond", "Club", "Spade"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
rank = 2
cards = []

for suit in suits:
    for value in values:
        cards.append(Card(suit, value, rank))
        rank += 1
    rank = 2

deck = Deck(cards)
random.shuffle(deck.cards)
player1_deck = Deck(cards[0:26])
player2_deck = Deck(cards[26:-1])

decision = input(
    "Welcome to War! (or Peace) This game will be played with 52 cards.\n"
    "The players today are Van and Kujo.\n"
    "Type \'GO\' to start the game!\n"
    "------------------------------------------------------------------\n")

if decision.upper() == "GO":
    van = Player("Van", player1_deck)
    kujo = Player("Kujo", player2_deck)

    turn = Turn(van, kujo)
    game = Game(van, kujo, turn)
    winner = game.start()
    print(winner + " Wins War or Peace")
else:
    print("Thanks for playing!")
