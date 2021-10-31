# task_9_5.py
#класс Stationery:
#атрибут 'title' и метод 'draw' --> «Запуск отрисовки»
#три дочерних класса Pen, Pencil, Handle
#в каждом классе реализовать переопределение метода draw

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f'class «{self.__class__.__name__}», атрибут: «{self.title}», метод :«Запуск отрисовки»')


class Pen(Stationery):
    def draw(self):
        return print(f'class «{self.__class__.__name__}», атрибут: «{self.title}», метод :«Запуск отрисовки»')


class Pencil(Stationery):
    def draw(self):
        return print(f'class «{self.__class__.__name__}», атрибут: «{self.title}», метод :«Запуск отрисовки»')


class Handle(Stationery):
    def draw(self):
        return print(f'class «{self.__class__.__name__}», атрибут: «{self.title}», метод :«Запуск отрисовки»')

t = [Stationery('stationery'),
     Pen('Pen'),
     Pencil('Pencil'),
     Handle('Handle')]
for i in t:
    i.draw()
# class «Stationery», атрибут: «stationery», метод :«Запуск отрисовки»
# class «Pen», атрибут: «Pen», метод :«Запуск отрисовки»
# class «Pencil», атрибут: «Pencil», метод :«Запуск отрисовки»
# class «Handle», атрибут: «Handle», метод :«Запуск отрисовки»
