from card import Card
import random

class CardDeck:
  'A class for a simple 52-card deck'

  def __init__(self):
    #self.deck = {'Clubs': Suit('clubs'), 'Diamonds': Suit('diamonds'), 'Hearts': Suit('hearts'), 'Spades': Suit('spades')}
    self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    self.deck = []

    for i in self.suits:
      for j in range(2,15):
        self.deck.append(Card(i, j))

    random.shuffle(self.deck)

  def drawCard(self):
    return self.deck.pop()

  def getDeck(self):
    return self.deck

  def setDeck(self, deck):
    self.deck = deck

  def getNumberOfCards(self):
    return len(self.deck)

    return sum

  def isEmpty(self):
    return self.getNumberOfCards() == 0
