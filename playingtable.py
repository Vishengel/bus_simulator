from carddeck import CardDeck

class PlayingTable:
  'A class for the playing table containing the cards'

  def __init__(self, numberOfCards):
    self.deck = CardDeck()
    self.cardsOnTable = []
    self.numberOfCards = numberOfCards

    self.dealCards(self.numberOfCards)

  def dealCards(self, numberOfCards):
    for x in range(0, numberOfCards):
      self.cardsOnTable.append(self.deck.drawCard())

  def printCardsOnTable(self, cardNo):
    print "-------------------------------"
    print "Cards currently on the table:"
    print "-------------------------------"
    for c in self.cardsOnTable:
      print (c.getType()),
      if self.cardsOnTable.index(c) == cardNo:
        print "<"
      else:
        print ""
    print "-------------------------------"

  def getCardsOnTable(self):
    return self.cardsOnTable
  
  def getNumberOfCardsInDeck(self):
    return self.deck.getNumberOfCards()

  def getCardTypesOnTable(self):
    cardTypesOnTable = [c.getType() for c in self.cardsOnTable]
    return cardTypesOnTable

  def replaceCard(self, cardNo, card):
    self.cardsOnTable[cardNo] = card

  def getDeck(self):
    return self.deck

  def deckIsEmpty(self):
    return self.deck.isEmpty()

  def reshuffleDeck(self):
    self.deck = CardDeck()
    
    for c in self.deck.getDeck():
      self.deck.setDeck( [c for c in self.deck.getDeck() if c.getType() not in self.getCardTypesOnTable()] )
