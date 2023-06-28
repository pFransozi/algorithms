import collections
from random import choice

# allow access the attributes by names instead of position index.
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') #listcomp
    suits = 'spades diamonds clubs hearts'.split()

    #  Called after the instance has been created (by __new__()), but before it is returned to the caller.
    # __new__() to create it, and __init__() to customize it
    def __init__(self) -> None:
        self._cards =  [Card(rank, suit) for suit in self.suits
                                         for rank in self.ranks]
    
    # Called to implement the built-in function len().
    def __len__(self):
        return len(self._cards)
    
    # called to implement evaluation of self[key]. gives the support to slicing, iteration, reverse.
    def __getitem__(self, position):
        return self._cards[position]