# OOP motivation
* The general rule is that first we need to identify if we need to apply OOP in the first place
* Usually, if there are situations where there is a relation between data and behaviour, we can start to think of applying OOP
* The following example shows this relation
```python
Point = Tuple[float, float]

def distance(p1: Point, p2: Point) -> float:
   return hypot(p1[0] - p2[0], p1[1] - p2[1])

Polygon = List[Point]

def perimeter(polygon: Polygon) -> float:
    pairs = zip(polygon, polygon[1:] + polygon[:1])
    return sum(distance(p1, p2) for p1, p2 in pairs)
```
* We can see that there is clearly a relation beteen ```Polygon``` and the ```perimeter``` method since perimeter operates on polygons
* Also, in the future if we have more mathematical function, then encapsulating them all together seems a good approach
* Also, the above statements are true for the Point class as well since distance is calculated between two points
* Therefore, the above program can be written in an OOP way as follows:
```python
class Point:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def distance(self, other: "Point") -> float:

        """

        Accepts another Point object to calculate the distance
        """
        return hypot(self.x - other.x, self.y - other.y)

class Polygon:

    def __init__(self, vertices: Optional[Iterable[Point]]) -> None:
        self.vertices = list(vertices) if vertices else []

    def perimeter(self) -> float:
        pairs = zip(self.vertices, self.vertices[1:] + self.vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)

```
--- 
# Properties
## Why do we need them
* In python, there is no concept of private variables
* In traditional languages, we have getters and setters to set the variable value
* If we want to do some checking on the value before assignment, we could use getters and setters, but this is not the pythonic way
* In python, we use the **property** function to make methods that look like attributes
* The following example shows this:
```python
class S:
    def __init__(self, name: str, age: int) -> None:
        self._age = age
        self._name = name # _name denotes a private attribute

    def _set_name(self, name:str) -> None:
        if name == "" or name == "John":
            raise ValueError("Empty and John are not allowed")
        self._name = name
    def _get_name(self) -> str:
        return self._name

    name = property(_get_name, _set_name)
"""
>>> s = S("aa", 12)
>>> s.name
aaa
>>> s.name = ""
Value Error: "Empty and John are not allowed"
"""
```
* It is useful in cases when we want to perform any operation (logging, deleting, updating) when updating the variable
## Using decorators for properties
* We can also use decorators to act as a short hand syntax shown below:
```python
class A:
    def __init__(self, name: str) -> None:
        self._name = name
        self._state: str
    
    @property
    def foo(self) -> str:
        print("Getting {self._name}'s state")
        return self._state
    
    @foo.setter  # Name should exactly be same as the property
    def foo(self, state: str) -> None:
        print(f"Setting {self._name}'s State to {state!r}")
        self._state = state 
```
---
# When to use properties
* When we want to do some action when modifying the attributes, then properties can be a good option
* Custom getters can be used to perform calculation on the fly as shwon below:
```python
class AvgList(List[int]):  # Inherting base class to get access to all the values

    @property
    def average(self) -> float:
        return sum(self) / len(self)

"""
>>> a = AvgList([1,2,3,4,62,3,32])
>>> a.avg
23.2
"""
```
* Custom setters can useful for data validation