import random

class Game:
    def __init__(self, player1, player2, turn):
        self.player1 = player1
        self.player2 = player2
        self.turn = turn

    def start(self):
        self.turn_logic()
        return self.game_winner()

    def turn_logic(self):
        turn_count = 0
        while not (self.player1.has_lost() or self.player2.has_lost() or turn_count == 1000000):
            winner = self.turn.winner()
            if winner == "No Winner":
                print("Mutually Assured Destruction 6 card have been removed from play")
                self.turn.pile_cards()
            else:
                print("Turn" +str(turn_count) + self.turn.type() + ": " + str(winner.name) + " has won the game")
                self.turn.pile_cards()
                print(str(len(self.turn.spoils)) + " cards!")
                self.turn.award_spoils(winner)
            turn_count += 1

    def game_winner(self):
        if self.player1.has_lost():
            return self.player2.name
        else:
            return self.player1.name
