"""
Отрезок в пространстве

Добавьте к реализованному в задании № 1 классу Point3D класс Segment3D, представляющий отрезок. Конструктор должен принимать пару точек — концы отрезка. Класс должен реализовывать два метода:
●     length — не принимает аргументов, возвращает длину отрезка;

●     middle — не принимает аргументов, возвращает точку (экземпляр класса Point3D), находящуюся в середине отрезка.
Пример работы программы:
p1 = Point3D(1, 2, 3)
p2 = Point3D(2.5, 1, -2)
s = Segment3D(p1, p2)
s.length()
5.315072906367325
m = s.middle()
type(m) == Point3D->True
m.x->1.75
m.y->1.5
m.z->0.5
"""
import math


class Point3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        distance = math.sqrt(
            pow(abs(self.x - other.x), 2) + pow(abs(self.y - other.y), 2) + pow(abs(self.z - other.z), 2))
        return distance


class Segment3D(Point3D):
    def __init__(self, p1, p2):
        Point3D.__init__(self, p1.x, p1.y, p1.z)
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance_to(self.p2)

    def middle(self):
        x = (self.p1.x + self.p2.x) / 2
        y = (self.p1.y + self.p2.y) / 2
        z = (self.p1.z + self.p2.z) / 2
        return Point3D(x, y, z)


if __name__ == '__main__':
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(2.5, 1, -2)
    s = Segment3D(p1, p2)
    print(s.length())
    m = s.middle()
    print(isinstance(m, Point3D))  # is instance is better instead of comparing with type
    print(m.x)
