class InfiniteRepeater:

    def __init__(self, value) -> None:
        self.value = value

    # def __iter__(self) -> "RepeaterIterator":
    #     return RepeaterIterator(self)

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


class RepeaterIterator:

    def __init__(self, source: "InfiniteRepeater") -> None:
        self.source = source

    def __next__(self):
        return self.source.value

    
class BoundedRepeater:

    """
    
    Returns an iterator which runs till the given repetitions

    >>> o = BoundedRepeater("foo", 3)
    >>> for item in o:
    ...     print(item)
    ...
    foo
    foo
    foo
    
    """

    def __init__(self, value, max_repeats) -> None:
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value