from __future__ import annotations
from collections import abc
import bisect
from typing import Any, Iterable, Iterator, Sequence, Union, overload
from typing_extensions import Protocol

"""
The Lookup class implements a basic dict-like structure.
It implements the abstract methods present in the Mapping and the base classes.

>>> x = Lookup([["a", 1], ["b", 2]])
>>> x["a"]
1

>>> y = Lookup({"a": 1, "b": 2})
>>> y["a"]
1

"""
class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...


BaseMapping = abc.Mapping

class Lookup(BaseMapping):

    # @overload
    # def __init__(
    #     self, 
    #     source: Iterable[tuple[Comparable, Any]]
    # ) -> None:
    #     ...

    # @overload
    # def __init__(
    #     self,
    #     source: BaseMapping
    # ) -> None:
    #     ...

    def __init__(
        self,
        source: Union[Iterable[tuple[Comparable, Any]], BaseMapping, None] = None,
    ) -> None:

        """
        The constructor accepts either a list of tuples or a dict
        The Union type hint means that it can be on of the arguments        

        """
        sorted_pairs: Sequence[tuple[Comparable, Any]]
        if isinstance(source, Sequence):
            sorted_pairs = sorted(source)
        elif isinstance(source, abc.Mapping):
            sorted_pairs = sorted(source.items())
        else:
            sorted_pairs = []
        self.key_list = [p[0] for p in sorted_pairs]
        self.value_list = [p[1] for p in sorted_pairs]

    def __len__(self) -> int:
        return len(self.key_list)

    def __iter__(self) -> Iterator[Comparable]:
        return iter(self.key_list)
    
    def __contains__(self, key: object) -> bool:
        index = bisect.bisect_left(self.key_list, key)
        return key == self.key_list[index]
    
    def __getitem__(self, key: Comparable) -> Any:
        index = bisect.bisect_left(self.key_list, key)
        if key == self.key_list[index]:
            return self.value_list[index]
        raise KeyError(key)