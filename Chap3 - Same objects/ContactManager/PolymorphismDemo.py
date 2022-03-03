class BaseClass:
    def call(self) -> None:
        print("inside BaseClass")

class SubClassA(BaseClass):
    pass

class SubClassB(BaseClass):
    def call(self) -> None:
        print("inside SubClass B")


class User:

    """
    This is same as Java. The dist object has a typehint that it belongs to class BaseClass
    During execution, we use python's duck typing behaviour to call the correct method    
    
    This code shows Liskov Substitution
    
    >>> s = User(SubClassB())
    >>> s.call()
    inside SubClass B

    >>> s = User(SubClassA())
    >>> s.call()
    inside BaseClass

    """
    dist: BaseClass

    def __init__(self, obj: BaseClass) -> None:
        self.dist = obj

    def call(self) -> None:
        self.dist.call()