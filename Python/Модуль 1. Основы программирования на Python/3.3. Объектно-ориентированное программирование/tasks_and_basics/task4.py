"""
Игровой мир

Теперь нужно населить игровой мир различными существами. Ваш гейм-дизайнер придумал сложную разветвленную иерархию существ.

Во-первых, все существа делятся на земных, морских и воздушных. Среди земных существ выделяются тролли и эльфы, среди морских — русалки и сирены, среди воздушных — драконы и пегасы.

Создайте базовый класс Creature, а также его наследников:
●     EarthCreature (с подклассами Troll и Elf),
●     SeaCreature (с подклассами Mermaid и Siren),
●     AirCreature (с подклассами Dragon и Pegasus).

Никаких методов пока реализовывать не нужно, но каждый класс должен содержать атрибут health_points в соответствии с таблицей.

 Класс  Значение атрибута
        health_points

Troll     100

Elf        80

Mermaid    60

Siren      75

Dragon     120

Pegasus    85

Пример работы программы:
x = Elf()
isinstance(x, EarthCreature)  ⇒ True
isinstance(x, Creature)       ⇒ True
x.health_points               ⇒ 80
"""


class Creature:
    def __init__(self):
        pass


class EarthCreature(Creature):
    pass


class SeaCreature(Creature):
    pass


class AirCreature(Creature):
    pass


class Troll(EarthCreature):
    health_points = 100


class Elf(EarthCreature):
    health_points = 80


class Mermaid(SeaCreature):
    health_points = 60


class Siren(SeaCreature):
    health_points = 75


class Dragon(AirCreature):
    health_points = 120


class Pegasus(AirCreature):
    health_points = 85


if __name__ == '__main__':
    x = Elf()
    print(isinstance(x, EarthCreature))
    print(isinstance(x, Creature))
    print(x.health_points)
