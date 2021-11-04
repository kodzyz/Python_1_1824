# task_10_3.py
#класс : «Unit»
#integer : int
#методы : (__add__()), (__sub__()), (__mul__()),  (__truediv__())
#метод : Unit(15).make_order(5) *****\n*****\n*****...,

class Unit:
    def __init__(self, integer):
        self.integer = int(integer)

    def __str__(self):
        return f'{self.integer * "*"}'

    def __add__(self, other):
        return Unit(self.integer + other.integer)

    def __sub__(self, other):
        return Unit(self.integer - other.integer)

    def __mul__(self, other):
        return Unit(int(self.integer * other.integer))

    def __truediv__(self, other):
        return Unit(round(self.integer / other.integer))

    def make_order(self, _row):
        s = ''
        _i = int(self.integer / _row)
        for _ in range(_i):
            s += f'{"*" * _row}\\n'
        s += f'{"*" * (self.integer % _row)}'
        return s


c1 = Unit(15)
c2 = Unit(3)
print(c1)#***************
print(c2)#***
print(c1 + c2)#******************
print(c1 - c2)#************
print(c1 * c2)#*********************************************
print(c1 / c2)#*****
print(c1.make_order(7))#*******\n*******\n*
print('end')
