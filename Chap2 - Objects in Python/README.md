# Objects in Python
* When we write a **class** statement, it creates a new object of **type**
* In Python, we can assign type hints to a method in order to make it more readable. For e.g
```python

def odd(n: int) -> bool:
    return n%2 != 0
```
* They do not add any runtime overhead but can improve code readability
* In python OOP, the **self** argument to a class method is the reference of the object
```python
class abc:
    def reset(self):
        self.x = 0
        self.y = 0
```
* In reality, there is only 1 method which accepts different objects of the same class
---
# Python class naming convention
* [PEP8](https://www.python.org/dev/peps/pep-0008/) recommends **CapWords** styling 
* 