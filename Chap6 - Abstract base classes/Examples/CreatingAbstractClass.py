import abc
import random
from typing import Type

class Die(abc.ABC):

    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        ...     # Business logic will be implemented by the concrete class
    
    def __repr__(self) -> str:
        return f"{self.face}"

class D4(Die):

    def roll(self) -> None:
        self.face = random.choice((1, 2, 3, 4))

class D6(Die):

    def roll(self) -> None:
        self.face = random.randint(1, 6)


class Dice(abc.ABC):

    def __init__(self, n: int, die_class: Type[Die]) -> None:
        """
        The variable 'die_class' is the type of the class 

        """
        self.dice = [die_class() for _ in range(n)] # The constructor is called to create object instances

    @abc.abstractmethod
    def roll(self) -> None:
        ...
    
    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice)
    
class SimpleDice(Dice):

    """
    This class basically serves to call the business logic
    The implementation details are hidden in the super classes

    >>> sd = SimpleDice(5, D4)  # Creates 5 instances of D4 class
    >>> sd.roll()
    >>> sd.total
    36

    """

    def roll(self) -> None:
        for d in self.dice:
            d.roll()       # Rolling for each instance of Die
            