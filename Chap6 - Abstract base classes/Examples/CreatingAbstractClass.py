import abc
import random
from typing import Any, Type

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


# To simulate operator overloading, we implement another Dice class
class DDice:

    """
    This class demonstrates operator overloading
    We implement the __add__ and __radd__ built-in methods
    The same is true for other operators
    """
    def __init__(self, *die_class: Type[Die]) -> None:
        self.dice = [dc() for dc in die_class]
        self.adjust: int = 0

    def plus(self, adjust: int = 0) -> "DDice":
        self.adjust = adjust
        return self

    def roll(self) -> None:
        for d in self.dice:
            d.roll()
    
    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice) + self.adjust

    def __add__(self, die_class: Any) -> "DDice":
        if isinstance(die_class, type) and issubclass(die_class, Die):
            new_classes = [type(d) for d in self.dice] + [die_class]
            new = DDice(*new_classes).plus(self.adjust)
            return new
        elif isinstance(die_class, int):
            new_classes = [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(die_class)
            return new
        else:
            return NotImplemented

    def __radd__(self, die_class: Any) -> "DDice":
        return self.__add__(die_class)
        # if isinstance(die_class, type) and issubclass(die_class, Die):
        #     new_classes = [die_class] + [type(d) for d in self.dice] 
        #     new = DDice(*new_classes).plus(self.adjust)
        #     return new
        # elif isinstance(die_class, int):
        #     new_classes = [type(d) for d in self.dice]
        #     new = DDice(*new_classes).plus(die_class)
        #     return new
        # else:
        #     return NotImplemented

