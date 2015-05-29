from suit import Suit
import random

class CardDeck:
  'A class for a simple 52-card deck'

  def __init__(self):
    self.deck = {'Clubs': Suit('clubs'), 'Diamonds': Suit('diamonds'), 'Hearts': Suit('hearts'), 'Spades': Suit('spades')}

  def drawCard(self):
    while True:
      randomsuit = random.choice(self.deck.keys())
      if self.deck[randomsuit].getNumberOfCards() > 0:
        break

    return self.deck[randomsuit].drawCard()

  def getDeck(self):
    return self.deck

  def getNumberOfCards(self):
    sum = 0

    for key, value in self.deck.iteritems():
      sum += value.getNumberOfCards()

    return sum

  def isEmpty(self):
    return self.getNumberOfCards() == 0
