from typing import Any, Dict, Hashable, Iterable, Mapping, Tuple, Union, cast

from numpy import isin


class NoDuplicateKeyDict(Dict[Hashable, Any]):

    """
    Here, we are extending the Dict concrete class
    We check if the key is being duplicated or not

    """
    def __setitem__(self, key: Hashable, value: Any) -> None:
        
        if key in self:
            raise ValueError(f"Key {key!r} already present" )
        super().__setitem__(key, value)

    """
    
    The constructor can accept different types of parameter for initialization
    In the case of Iterable[Tuple], since we set the mapping by ourselves, it uses our custom __setitem__() method
    That is why the exception is raised

    In the case of Mapping[], since we call the super class directly, our __setitem__() is not called

    >>> d = NoDuplicateKeyDict({"a": 1, "b": 2})
    >>> d
    {'a': 4}

    >>> d = NoDuplicateKeyDict([["a", 1], ["b", 2]])
    >>> d
    {'a': 2, 'b': 1}

    >>> d = NoDuplicateKeyDict([["a", 1], ["a", 2]])
    ValueError: Key 'a' already present
    """
    def __init__(
        self, 
        init: Union[Iterable[Tuple[Hashable, Any]], Mapping[Hashable, Any], None] = None,
        **kwargs: Any
    ) -> None:
        if isinstance(init, Mapping):
            super().__init__(init, **kwargs)
        elif isinstance(init, Iterable):
            for k, v in cast(Iterable[Tuple[Hashable, Any]], init):
                self[k] = v
        elif init is None:
            super().__init__(**kwargs)
        else:
            super().__init__(init, **kwargs)
