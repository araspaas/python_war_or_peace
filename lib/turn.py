class Turn:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.spoils = []

    def type(self): # determines the type of turn "Basic", "War", or "Mutually Assured Destruction"
        if self.player1.deck.rank_of_card_at(0) == self.player2.deck.rank_of_card_at(0)\
                and self.player1.deck.rank_of_card_at(2) == self.player2.deck.rank_of_card_at(2):
            return "MAD"
        elif self.player1.deck.rank_of_card_at(0) != self.player2.deck.rank_of_card_at(0):
            return "basic"
        else:
            return "war"

    def winner(self):
        if self.type() == "basic":
            return self.find_basic_winner()
        elif self.type() == "war":
            return self.find_war_winner()
        else:
            return "No Winner"

    def find_basic_winner(self): # finds the winner of a basic turn
        if self.player1.deck.rank_of_card_at(0) > self.player2.deck.rank_of_card_at(0):
            return self.player1
        else:
            return self.player2

    def find_war_winner(self): # finds the winner of a war turn
        if self.player1.deck.rank_of_card_at(2) > self.player2.deck.rank_of_card_at(2):
            return self.player1
        else:
            return self.player2

    def pile_cards(self):
        if self.type() == "basic":
            return self.pile_basic()
        elif self.type() == "war":
            return self.pile_war()
        else:
            return self.pile_mad()

    def pile_basic(self): # Each player has a card go to the spoils pile winner gets both cards
        self.spoils.append(self.player1.deck.remove_card())
        self.spoils.append(self.player2.deck.remove_card())
        return self.spoils

    def pile_war(self): # Each player puts in 3 cards to the spoils pile. winner gets all 6 cards
        for card in range(0, 3):
            self.spoils.append(self.player1.deck.remove_card())
        for card in range(0, 3):
            self.spoils.append(self.player2.deck.remove_card())
        return self.spoils

    def pile_mad(self): # Each player puts 3 cards in the pile but tie and both players lose their cards.
        for card in range(3):
            self.player1.deck.remove_card()
        for card in range(3):
            self.player2.deck.remove_card()

    def award_spoils(self, winner):
        for c in self.spoils:
            winner.deck.add_card(c)
        self.spoils = []
