
import abc
from functools import wraps
import logging
import random
from typing import Any, Dict, Tuple, Type, cast

"""
This example demonstrates how we can use metaclasses 
to add additional behaviour to a concrete class method

"""

class DieMeta(abc.ABCMeta):

    def __new__(
        metaclass: Type[type], 
        name: str,  # Name of the target class
        bases: Tuple[type, ...],    # Base classes
        namespace: Dict[str, Any],  # Contains all the intermediate code waiting to build the final object
        **kwargs: Any   # Any extra arguments
    ) -> "DieMeta":
        if "roll" in namespace and not getattr(
            namespace["roll"], "__isbastractmethod__", False
        ):
            namespace.setdefault("logger", logging.getLogger(name))     # Introduce a new logger

            original_method = namespace["roll"]     # Get the method 

            @wraps(original_method)     # Transfers all the docstrings to this new method
            def logged_roll(self: "DieLog") -> None:    
                original_method(self)   # Call the original method
                self.logger.info(f"Rolled {self.face}")     # Call our logic

            namespace["roll"] = logged_roll     # Assign back the modified method


        new_object = cast("DieMeta", abc.ABCMeta.__new__(
            metaclass, name, bases, namespace
        ))      # Create the final class object

        return new_object


class DieLog(metaclass=DieMeta):

    logger: logging.Logger

    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        ...

    def __repr__(self) -> str:
        return f"{self.face}"

class D6L(DieLog):

    """
    Logs all the calls to the roll method due to metaclass

    >>> import sys
    >>> logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    >>> d = D6L()
    INFO:D6L:Rolled 3

    >>> d.roll()
    INFO:D6L:Rolled 1
    
    """

    def roll(self) -> None:
        self.face = random.randrange(1, 7)


