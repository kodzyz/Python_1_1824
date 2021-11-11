#класс «Комплексное число»
# Реализовать перегрузку методов сложения и умножения комплексных чисел.
#выполнить сложение и умножение созданных экземпляров

class MPMCatErr(Exception):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return f'"{self.text}"'

class Complex:
    def __init__(self, real=0, imag=0, *args):
        if isinstance(real, str):
            raise MPMCatErr(f'"{real}" - "только не тип "str"')
        elif isinstance(imag, str):
            raise MPMCatErr(f'"{imag}" - "только не тип "str"')
        elif len(args) != 0:
            raise MPMCatErr(f'много лишнего, однако: {args}')
        self.real = real
        self.imag = imag
        self.z = 'a+b*j'
        self.complex = self

    def __add__(self, other):
        if isinstance(other, Complex):
            self.real_part = self.real + other.real
            self.imag_part = self.imag + other.imag
            return f'({self.check(self.real, self.imag)}) + ({self.check(other.real, other.imag)}) = {self.check(self.real_part, self.imag_part)}'
        else:
            raise MPMCatErr(f'"{other}" - это не из нашего экземпляра')

    def __mul__(self, other):
        if isinstance(other, Complex):
            self.real_part = ((self.real * other.real) - (self.imag * other.imag))
            self.imag_part = ((self.imag * other.real) + (self.real * other.imag))
            return f'({self.check(self.real, self.imag)}) * ({self.check(other.real, other.imag)}) = {self.check(self.real_part, self.imag_part)}'
        else:
            raise MPMCatErr(f'"{other}" - это не из нашего экземпляра')

    def __str__(self):
        return f'{self.check(self.real, self.imag)}'

    @staticmethod
    def check(a, b):
        if a == 0 and b < 0:
            return f'{b}j'
        elif a == 0 and b >= 0:
            return f'{b}j'
        elif a != 0 and b < 0:
            return f'{a}{b}j'
        else:
            return f'{a}+{b}j'


print('"Мой результат:"')
try:
    z_1 = Complex(0, -8)
    z_2 = Complex(-5, 3)
    print(z_1)
    print(z_2)
    print(z_1 + z_2)
    print(z_1 * z_2)
except TypeError as e:
    print(f'unsupported operand type(s) for "class Complex"')
except MPMCatErr as e:
    print(e)

print('"Проверка встроенной ф-й complex():')
a = 0 + -8j
b = -5 + 3j
print(complex(a+b))
print(complex(a*b))
'''Расчет:'''
# "Мой результат:"
# -8j
# -5+3j
# (-8j) + (-5+3j) = -5-5j
# (-8j) * (-5+3j) = 24+40j
# "Проверка встроенной ф-й complex():
# (-5-5j)
# (24+40j)
'''Проверка на валидность:'''
#z_1 = Complex(0, -8, 0, -8)
#"много лишнего, однако: (0, -8)"

#print(z_1 + 0)
#""0" - это не из нашего экземпляра"

#z_2 = Complex(-5, '3')
#""3" - "только не тип "str""

#print(7 + z_2)
# unsupported operand type(s) for "class Complex"