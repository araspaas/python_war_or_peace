class Deck:

    def __init__(self, cards): #creating a deck of cards.
        self.cards = cards

    def rank_of_card_at(self, index): #checking the rank of a card in the deck.
        return self.cards[index].rank if self.cards else 0

    def high_ranking_cards(self): # Checking for cards that rank above 10.
        return [card for card in self.cards if card.rank > 10]

    def percent_high_ranking(self): # Checking in a deck the percentage of cards that are high ranking cards (above 10)
        return (len(self.high_ranking_cards())/len(self.cards))*100 if self.high_ranking_cards() else 0

    def remove_card(self): # remove card from deck
        return self.cards.pop(0)

    def add_card(self, card): # Add card to deck
        self.cards.append(card)

# import ipdb; ipdb.set_trace() <---- this is similar to Ruby's binding.pry for debugging
