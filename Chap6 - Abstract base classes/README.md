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
