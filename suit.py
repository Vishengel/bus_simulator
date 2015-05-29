from card import Card
import random

class Suit:
  'A class representing the Suits of a deck'

  def __init__(self, suit):
    self.suit = suit
    self.cards = []

    for x in range(2,11):
      self.cards.append(Card(self.suit, x))

    self.cards.append(Card(self.suit, 'Jack'))
    self.cards.append(Card(self.suit, 'Queen'))
    self.cards.append(Card(self.suit, 'King'))
    self.cards.append(Card(self.suit, 'Ace'))

  def drawCard(self):
    randomCard = random.choice(self.cards)
    #print randomCard.getType()
    self.cards = [c for c in self.cards if c.getType()[1] != randomCard.getType()[1]]
    return randomCard

  def getsuit(self):
    return self.suit

  def getCards(self):
    return self.cards
  
  def resetCards(self, newCards):
    self.cards = newCards

  def getNumberOfCards(self):
    return len(self.cards)

  def printCards(self):
    print self.suit
    for x in self.cards:
      print x.getType()[1],
