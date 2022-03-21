from __future__ import annotations
from contextlib import contextmanager

from types import TracebackType
from typing import Any, Iterator, List, Optional, Type
from typing_extensions import Literal


class StringJoiner(List[str]):  # The argument to class is the datatype we are working on

    """
    >>> with StringJoiner("Hello") as sj:
    >>>     sj.append("World")
    >>>
    >>> sj.result
    >>> 'HelloWorld'
    """
    def __enter__(self) -> "StringJoiner":
        return self

    def __exit__(
        self, 
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> Literal[False]:
        self.result = "".join(self)
        return False


class StringJoiner2(List[str]):
    def __init__(self, *args: str):
        super().__init__(*args)
        self.result = "".join(self)

@contextmanager
def joiner(*args: Any) -> Iterator[StringJoiner2]:
    string_list = StringJoiner2(*args)
    try:
        yield string_list
    finally:
        string_list.result = "".join(string_list)