import abc


class MediaLoader(abc.ABC):         # Cannot be instantiated
    @abc.abstractmethod
    def play(self) -> None:
        ...
    
    @property           # Order of decorators matter
    @abc.abstractmethod
    def ext(self) -> str:
        ...

class MediaLoaderSimple(abc.ABC):   # This class can be instantiated since it does not have any abstract methods
    pass

class MediaLoaderNormalClass():

    """
    Since this class does not inherit from abc.ABC, 
    it does not prevent it's creation even when abstract methods are present
    """
    @abc.abstractmethod
    def play(self) -> None:
        ...