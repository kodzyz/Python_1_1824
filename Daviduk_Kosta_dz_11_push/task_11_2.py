# task_11_2.py
#Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
import re
from decimal import Decimal

class Err_zero(Exception):
    formula_format = 'x/y'
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Error division by zero {self.value}'

class InputErr(Err_zero):
    def __init__(self, value):
        super(InputErr, self).__init__(value)
    def __str__(self):
        return f'formula Error:{self.value}\n\t\t Enter the formula by format:"{self.formula_format}"'

class By_zero:
    re_data = re.compile(r'^(0|[1-9]\d*)([.,]\d+)?[/](0|[1-9]\d*)([.,]\d+)?$')
    re_data1 = re.compile(r'/')
    def __init__(self, formula=None):
        self.formula = formula
        if not By_zero.re_data.match(formula):
            raise InputErr(formula)
        elif By_zero.re_data.match(formula):
            a, b = map(Decimal, By_zero.re_data1.split(formula.replace(',', '.')))
            self.a = a
            self.b = b
            self.result = self.div_rez()
    def __str__(self):
        return f'{self.a} / {self.b} = {self.result}'
    def div_rez(self):
        if self.b != 0:
            result = self.a / self.b
            result = result.quantize(Decimal("1.00"))
            return result
        else:
            raise Err_zero(self.formula)

per = input('Enter "x/y" :  ')
try:
    h = By_zero(per)
    print(h)
except Err_zero as e:
    print((f'raise (msg:)\n {e}'))
# Enter "x/y" :  fghfghffghf
# raise (msg:)
#  formula Error:fghfghffghf
# 		 Enter the formula by format:"x/y"

# Enter "x/y" :  4t/67
# raise (msg:)
#  formula Error:4t/67
# 		 Enter the formula by format:"x/y"

# Enter "x/y" :  65,4/78.65
# 65.4 / 78.65 = 0.83

# Enter "x/y" :  76/0,0
# raise (msg:)
#  Error division by zero 76/0,0


