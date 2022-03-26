import math


class Circle:

    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, val: float) -> None:
        self._radius = val

    @property
    def area(self) -> float:
        return self.pi() * self.radius**2

    def cylinder_volume(self, height: float) -> float:
        return self.area * height

    @classmethod
    def create_unit_circle(cls) -> "Circle":
        return cls(1)

    @staticmethod
    def pi() -> float:
        return math.pi

