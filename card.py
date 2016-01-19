class Card:
  'A class representing a single card'

  def __init__(self, suit, card):
    self.suit = suit
    self.value = card

    if card == 11:
      self.card = 'Jack'
    elif card == 12:
      self.card = 'Queen'
    elif card == 13:
      self.card = 'King'
    elif card == 14:
      self.card = 'Ace'
    else:
      self.card = card

  def getType(self):
    return (self.suit, self.card)

  def getValue(self):
    return self.value
