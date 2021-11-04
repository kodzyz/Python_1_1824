# task_10_1.py
#Реализовать класс Matrix
#Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

from operator import add

class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        return self.matrix_print(self.matrix)

    def __add__(self, other):
        _list = []
        for i in range(len(self.matrix)):
            _list.append(list(map(add, self.matrix[i], other.matrix[i])))
        return self.matrix_print(_list)

    def matrix_print(self, m):
        self.m = m
        _str = ''
        for i in m:
            _str += f"{', '.join(map(str, i))}\n"
        return _str

x = [[4, 6, 3, 8], [10, 3, 2, 7], [1, 3, 2, 2]]
y = [[1, 10, 9, 3], [1, 3, 5, 3], [1, 3, 8, 3]]

m1 = Matrix(x)
m2 = Matrix(y)
print(m1)
print(m2)
print(m1 + m2)
# 4, 6, 3, 8
# 10, 3, 2, 7
# 1, 3, 2, 2
#
# 1, 10, 9, 3
# 1, 3, 5, 3
# 1, 3, 8, 3
#
# 5, 16, 12, 11
# 11, 6, 7, 10
# 2, 6, 10, 5
print('end')