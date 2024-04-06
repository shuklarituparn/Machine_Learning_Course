"""
Точка в трехмерном пространстве

Реализуйте класс Point3D, представляющий точку в трехмерном пространстве. Конструктор должен принимать три аргумента: x,y,z

— координаты точки. Класс должен реализовывать метод distance_to, принимающий в качестве аргумента другую точку и возвращающий расстояние между ними.

Подробнее про вычисление расстояния можно прочитать в источнике.

Пример работы программы:

p1 = Point3D(1, 2, 3)
p2 = Point3D(2.5, 1, -2)
p1.distance_to(p2)

5.315072906367325

p1.x ->1
p1.y->2
p1.z->3
"""
import math


class Point3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        distance = math.sqrt(pow(abs(self.x - other.x), 2) + pow(abs(self.y - other.y), 2) + pow(abs(self.z - other.z), 2))
        return distance


if __name__ == '__main__':
    p1 = Point3D(1, 2, 3)  # so the class is working, now need to implement the methods
    p2 = Point3D(2.5, 1, -2)
    print(p1.distance_to(p2))
    print(p1.x)
    print(p1.y)
    print(p1.z)
