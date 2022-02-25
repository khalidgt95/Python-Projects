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
* To pass an object to a method, we can use the following type hint:
```python
class Point:
    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
```
* In python, the constructor is called as below:
 ```python
class Point:
    def __init__(self, 
                 x: float = 0, 
                 y: float = 0
            ) -> None:
            pass

    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
```
---
# Python class naming convention
* [PEP8](https://www.python.org/dev/peps/pep-0008/) recommends **CapWords** styling 
---
# Python Documentation
* We can run **doctest** to test if our documentation is correct or not
```
python -m doctest <python_file>.py
```
* We can also use **mypy** to test if our type hints are working correctly or not
```
mypy --strict <python_file>.py
```
---
# Virtual Environments
* To create a virtual environment, we can use the following syntax
```
$> python -m venv <my_environment_name>
$> source <my_environment_name>/bin/activate
```