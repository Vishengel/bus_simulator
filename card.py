class Card:
  'A class representing a single card'

  def __init__(self, suit, card):
    self.suit = suit
    self.card = card
    self.value = 0

    if card == 'Jack':
      self.value = 11
    elif card == 'Queen':
      self.value = 12
    elif card == 'King':
      self.value = 13
    elif card == 'Ace':
      self.value = 14
    else:
      self.value = card

  def getType(self):
    return (self.suit, self.card)

  def getValue(self):
    return self.value
