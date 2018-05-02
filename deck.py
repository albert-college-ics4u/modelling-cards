from cards import *

class Deck():

  def __init__(self):
    ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    suits = ['Hearts','Diamonds','Spades','Clubs']
    self.cards = []

    for s in range(len(suits)):
      for r in range(len(ranks)):
        self.cards.append( Card(ranks[r], suits[s]) )

  # Removes a single card from the top of the deck
  def draw(self):
    return self.cards.pop(0)

  # Draws a hand of n cards from the top of the deck
  def drawHand(self,n):
    hand = []
    for i in range(n):
      hand.append( self.cards.pop(0) )
    return hand

  # Looks at the top card in the deck without removing it
  def top(self):
      return self.cards[0]

  # Looks at the bottom card in the deck without removing it
  def bottom(self):
      return []

  # Create a method that will shuffle the deck
  def shuffle(self):
    return []

  # Create a method that will sort the deck
  # Hearts before Diamonds before Spades before Clubs
  def sort(self):
    return []