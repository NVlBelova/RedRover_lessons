import math
from abc import ABCMeta, abstractmethod


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Shape:
    def square(self) -> float:
        raise NotImplemented


class Square(Shape):
    def __init__(self, leftBottomPoint: Point, length: float) -> None:
        self.__leftBottomPoint = leftBottomPoint
        self.__leftTopPoint = Point(x=leftBottomPoint.x, y=leftBottomPoint.y + length)
        self.__rightBottomPoint = Point(x=leftBottomPoint.x + length, y=leftBottomPoint.y)
        self.__rightTopPoint = Point(x=leftBottomPoint.x + length, y=leftBottomPoint.y + length)
        self.__length = length

    def square(self) -> float:
        return self.__length ** 2


class Circle(Shape):
    def __init__(self, point, radius):
        self.__point = Point(point.x, point.y)
        self.__radius = radius

    def square(self) -> float:
        return math.pi * (self.__radius ** 2)


shapes = [Square(Point(0, 0), 5), Circle(Point(1, 2), 5), Square(Point(1, 1), 2)]

totalSquare = 0
for shape in shapes:
    totalSquare += shape.square()

print(totalSquare)
