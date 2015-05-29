from playingtable import PlayingTable
import sys
import random

class Simulation:
  'A class for simulation a set number of rounds of Ride the Bus'
  
  def __init__(self, busLength, reshuffleWhenEmpty, numberOfRounds):
    self.busLength = busLength
    self.reshuffleWhenEmpty = reshuffleWhenEmpty
    self.numberOfRounds = numberOfRounds
    
    self.table = PlayingTable(self.busLength)
    self.hasWon = False
    self.cardNo = 0
    self.totalDrinks = 0
    
    
  def run(self):
    for i in range(0, self.numberOfRounds):
      self.totalDrinks += self.playRound()
    
    print "Total number of drinks: ", self.totalDrinks
    average = float(self.totalDrinks)/float(self.numberOfRounds)
    print "Average number of drinks per round: %.2f" % average
    
  def playRound(self):
    totalDrinksThisRound = 0
    
    while not self.hasWon:
      drinks = 0
      
      #If the rule is that you continue even when the deck is empty, reshuffle the deck when it is empty
      if self.table.deckIsEmpty() and self.reshuffleWhenEmpty:
	self.table.reshuffleDeck()
      
      #Retrieve the card at the current position in the bus
      currentCard = self.table.getCardsOnTable()[self.cardNo]
      
      #Determine the next move
      answer = self.determineMove(currentCard.getValue())
      
      #Draw a card from the deck
      drawnCard = self.table.getDeck().drawCard()

      if self.determinePass(drawnCard.getValue(), currentCard.getValue(), self.busLength, answer):
	self.table.replaceCard(self.cardNo, drawnCard)
	self.cardNo += 1
	
	#Check whether the final card is reached. If true, return the total number of drinks
	if self.cardNo == self.busLength:
	  #Reset the playing table
	  self.cardNo = 0
	  self.table = PlayingTable(self.busLength)
	  
	  return totalDrinksThisRound

      else:
	drinks += (self.cardNo + 1)
	totalDrinksThisRound += drinks
	self.table.replaceCard(self.cardNo, drawnCard)
	self.cardNo = 0
	
  def determineMove(self, busValue):
    #We never make the move 'equal'
    
    #Say 'higher' if the card is 7 or lower
    if busValue < 8:
      return 'q'
    
    #Say 'lower' if the card is 9 or higher
    if busValue > 8:
      return 'z'
    
    #When the card has the value 8, there's a 50% chance of saying either 'higher' or 'lower' 
    return 'q' if random.randint(0,1) == 0 else 'z' 

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