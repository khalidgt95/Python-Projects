from typing import Optional

databaseGlobalObject: Optional[str] = None

class Point:

    """
    Represent a point in 2D

    >>> p_0 = Point()
    >>> p_1 = Point(1, 4)
    >>> p_1.x
    1
    """
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize a new point.
        :param x: x coordinate
        :param y: y coordinate
        """
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        """
        Move a point to a specified location
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        Reset point's location to the origin
        """
        self.move(0, 0)

    def check_optional_argument(self, x: Optional[str] = None) -> None:
        """
        
        In this function, we see how we can reference an object declared
        outside the function. Also, we see the use of Optional type hint
        """
        
        global databaseGlobalObject
        pass

