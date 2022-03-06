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