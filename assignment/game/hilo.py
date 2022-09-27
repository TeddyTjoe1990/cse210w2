import random

class Hilo:
  """
  Individual cards are represented as a number from 1 to 13.
  Current card will be shown.
  The next card will be shown.
  """
  def __init__(self) -> None:
    """
    Initialize two random cards.
    """
    self.card1 = random.randint(1, 13)
    self.card2 = random.randint(1, 13)
  
  def show_card1(self):
    """
    Display first card to player to start the game.
    """
    card_result = f'The card is: {self.card1}'
    print(card_result)
    
  def show_card2(self):
    """
    Display second card to player.
    """
    card_result = f'The card is: {self.card2}'
    print(card_result)
    
  def high_or_low(self):
    """
    Check if card is high or low.
    """
    if self.card2 > self.card1: #check for high card
      return 1
    elif self.card2 < self.card1: #check for the low card
      return 0
    else:
      return -1