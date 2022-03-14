# Abstract Classes
* To make a class abstract, we import from the ```abc.ABC``` special python class
* To define abstract methods, we use ```@abc.abstractmethod``` decorator
* ```abc.ABC``` class class prevents creation of objects in case abstract methods are present
* Normal class won't check this and can cause runtime errors
```python
class AbsClass(abc.ABC):

    @abc.abstractmethod
    def run(self) -> None:
        ... # Special syntax which means that it needs to be implemented
```
---
# Abstract class Collections
* The base class of collections is the container class
```
                            Container
                                |
                                |
                                |
                           Collections
                             /  |  \ 
                            /   |   \
                           /    |    \
                         List  Dict  Tuples   . . . 
```
* We can also extend the collections classes to create our own datatypes
---
# The collections.abc module
* This module provides the abstract base class definitions for built-in collections such as ```list```, ```set``` or ```dict```
* Let's consider the example of the concrete ```dict``` class
* It's inheritance diagram can be seen as below:
```
        (A)Container           (A)Iterable       (A)Sized
        + __contains__(item)   + __iter__()      +__len(item)

                        \           |           /
                          \         |         /
                            \       |       /
                              \     |     /
                                \   |   /
                              (A)Collection
                                    |
                                    |
                                (A)Mapping
                                + __getitem__(key)
                                + keys()
                                + items()
                                + values()
                                + get(key, default)  
                                    |
                                    |
                                (A)MutableMapping
                                + __setitem__(key, value)
                                + __delitem__(key)
                                    |
                                    |
                                  dict
```
---
# Creating own abstract base classes 
* In the file ```CreatingAbstractClass.py``` we give the example of defining our own abstract class to simulate a dice game
* The structure of the abstract classes goes from the most generic to specialized business logic
---
# Operator Overloading
* Most of the numerical operators such `+`, `-`, `/`, etc. call special methods under the hood
* In the example of `+`, it calls the `__add__()` method of the class
* In the following piece of code, we can see how we can change the default behaviour
```python
class A:

    def __init__(self) -> None:
        ...
    
    def __add__(self, class_type: Any) -> "A":
        ...
    
    def __radd__(self, class_type: Any) -> "A":
        ...
```
* Since the operations need to be commutative, we need to implement both `__add__` and `__radd__` to cover cases like `A + 6` or `6 + A`:
* 