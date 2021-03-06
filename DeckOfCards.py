import random

class DealDeck:
    def __init__(self):
        self.Cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.Suits=['♦','♣','♥','♠']
        self.RawDeck=[]
        self.ShuffledDeck=[]
        self.MakeDeck()

    def MakeDeck(self):
        for Card in self.Cards:
            for Suit in self.Suits:
                self.RawDeck.append('{0}{1}'.format(Card,Suit))
        self.ShuffleDeck()

    def ShuffleDeck(self):
        CardsInDeck=int(len(self.RawDeck))
        for each in range(CardsInDeck):
            Pick=random.randint(0,int(len(self.RawDeck))-1)
            self.ShuffledDeck.append(self.RawDeck[Pick])
            self.RawDeck.pop(Pick)
        return self.ShuffledDeck

    def __iter__(self):
        return iter(self.ShuffledDeck)
