# task_10_2.py
# Расчёт суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и
# проверить работу декоратора @property.


from abc import ABC, abstractmethod


class Material(ABC):
    @abstractmethod
    def costs(self):
        pass

class Coat:
    def __init__(self, value):
        self.v = value
        self.costs = round((self.v / 6.5 + 0.5), 1)

    @property
    def value(self):
        print('расход ткани по пальто ')
        return self.costs

    @value.setter
    def value(self, v):
        self.costs = round((v / 6.5 + 0.5), 1)
        return self.costs

    def costs(self):
        pass


class Costume:
    def __init__(self, value):
        self.h = value
        self.costs = round((2 * self.h + 0.3), 1)

    @property
    def value(self):
        print('расход ткани для костюма')
        return self.costs

    @value.setter
    def value(self, h):
        self.costs = round((2 * h + 0.3), 1)

    def costs(self):
        pass


class Clothes:
    def __init__(self, v, h):
        self.w = [Coat(v)] + [Costume(h)]

    def costs(self):
        main_costs = 0
        for i in self.w:
            main_costs += i.costs
        print('общий подсчёт расхода ткани')
        return main_costs


h = Clothes(3, 1)
c = Coat(3)
k = Costume(1)

print(c.value)
print(k.value)
print(h.costs())
print()
# расход ткани по пальто
# 1.0
# расход ткани для костюма
# 2.3
# общий подсчёт расхода ткани
# 3.3

c.value = 6.5
k.value = 2
h = Clothes(6.5, 2)

print(k.value)
print(c.value)
print(h.costs())

# расход ткани для костюма
# 4.3
# расход ткани по пальто
# 1.5
# общий подсчёт расхода ткани
# 5.8






	




