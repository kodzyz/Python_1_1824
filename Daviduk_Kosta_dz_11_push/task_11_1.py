## task_11_1.py
# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import re
import datetime

class Data:
    re_data = re.compile(r'(?:\d{2}[-]){2}\d{4}')
    re_data1 = re.compile(r'-')

    def __init__(self, data):
        if Data.re_data.match(data):
            self.data = str(data)
            #self.extract(self.data)

    @classmethod
    def extract(cls, data):
        if cls.re_data.match(data):
            number, month, year = map(int, cls.re_data1.split(data))
        else:
            raise ValueError(f'ValueError: {data}, правильный формат: «день-месяц-год»')
        if cls.validat(number, month, year):
            cls.str(cls, number, month, year)


    def str(self, number, month, year):
        return print(f' число:{number} -> тип:{type(number)}, '\
               f'месяц:{month} -> тип:{type(month)}, '\
               f'год:{year} -> тип:{type(year)}')

    def __str__(self):
        return f'"для извлечения используйте метод:" extract({self.data})"\n'

    @staticmethod
    def validat(number, month, year):
        try:
            return datetime.date(year, month, number)
        except ValueError as e:
            print(f'\nНеверный фомат даты:\t{e}\n')


try:
    d = Data('24-01-2021')
    print(d)
    d.extract('13-12-1980')
    d.extract('13-50-1980')
    d.extract('15-32 2021')
except ValueError as e:
    print(f'raise ValueError(msg:)\n {e}')

# "для извлечения используйте метод:" extract(24-01-2021)"
#
#  число:13 -> тип:<class 'int'>, месяц:12 -> тип:<class 'int'>, год:1980 -> тип:<class 'int'>
#
# Неверный фомат даты:	month must be in 1..12
#
# raise ValueError(msg)
#  ValueError: 15-32 2021, правильный формат: «день-месяц-год»