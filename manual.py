from playingtable import PlayingTable
import sys

class Manual:
  'A class for manually playing a single round of Ride the Bus'

  def __init__(self, busLength, reshuffleWhenEmpty):
    self.busLength = busLength
    self.reshuffleWhenEmpty = reshuffleWhenEmpty
    
    self.table = PlayingTable(busLength)
    self.hasWon = False
    self.cardNo = 0
    self.totalDrinks = 0
    
  def run(self):  
    print "Number of cards left in deck: ", self.table.getNumberOfCardsInDeck()

    while not self.hasWon:
      drinks = 0
      
      if self.table.deckIsEmpty() and self.reshuffleWhenEmpty:
	print "Reshuffling deck"
        self.table.reshuffleDeck()
        print "Number of cards left in deck: ", self.table.getNumberOfCardsInDeck()

      currentCard = self.table.getCardsOnTable()[self.cardNo]

      self.table.printCardsOnTable(self.cardNo)

      print ""
      print "Current card: ", currentCard.getType()
      print ""
      answer = raw_input("Higher (q), equal (a) or lower (z)?")

      drawnCard = self.table.getDeck().drawCard()
      print ""
      print "Drawn card: ", drawnCard.getType()
      print ""

      if self.determinePass(drawnCard.getValue(), currentCard.getValue(), self.busLength, answer):
        print "Correct!"
        self.table.replaceCard(self.cardNo, drawnCard)
        self.cardNo += 1

        if self.cardNo == self.busLength:
          print "You won!"
          print "Total number of drinks taken: ", self.totalDrinks
          sys.exit()

      else:
        print "False :("
        drinks += self.cardNo + 1
        self.totalDrinks += drinks
        print "You have to take %d drinks." % drinks
        self.table.replaceCard(self.cardNo, drawnCard)
        self.cardNo = 0
        
      print "Number of cards left in deck: ", self.table.getNumberOfCardsInDeck()

  def determinePass(self, drawnValue, busValue, busLength, answer):
    if drawnValue > busValue:
      if answer == 'q':
        return True
      else:
        return False

    if drawnValue < busValue:
      if answer == 'z':
        return True
      else:
        return False

    if (drawnValue == busValue) and (busLength == 9 or answer == 'a'):
      return True
    else:
      return False
