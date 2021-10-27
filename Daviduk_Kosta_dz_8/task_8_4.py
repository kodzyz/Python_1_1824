# task_8_4.py

# Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?
from functools import wraps


def type_logger(func):
   @wraps(func)
   def tag_wrapper(*args, **kwargs):
      # for i in args:
      #    print(f'{func.__name__}({i}: {type(i)})')
      # for i in kwargs.values():
      #    print(f'{func.__name__}({i}: {type(i)})')
      try:
         return_arg = list(map(func, args))
         return_kwa = list(map(func, kwargs.values()))
         return_arg.extend(return_kwa)
         return_arg = list(map(str, return_arg))
         return_calc_arg = ', '.join(return_arg)
         return return_calc_arg
      except TypeError as e:
         print(f'TypeError: {e}\n "To get the result, enter integers"')
   return tag_wrapper


def val_checker(argument):
   def _logger(func):
      def wrapper(*args, **kwargs):
         for i in args:
            if argument(i):
               print(f'a = {func.__name__} ({i})')
            else:
                raise ValueError(f'ValueError: wrong val {i}')
         for i in kwargs.values():
            if argument(i):
               print(f'a = {func.__name__} ({i})')
            else:
                raise ValueError(f'ValueError: wrong val {i}')
         result = func(*args, **kwargs)
         return result
      return wrapper
   return _logger


@val_checker(lambda x: x > 0)
@type_logger
def calc_cube(x):
   return x ** 3
try:
   a = calc_cube(5, 4, h=2, g=3.3)
   print(a)
except TypeError as e:
   print(f'myTypeError --> {e}')
except ValueError as e:
    print(f'     raise ValueError(msg)\n {e}')

#a = calc_cube(5, 4, h=2) --> a = calc_cube (5)
#                             a = calc_cube (4)
#                             a = calc_cube (2)
#                             125, 64, 8

#a = calc_cube(5, -4) --> a = calc_cube (5)
#                         raise ValueError(msg)
#                      ValueError: wrong val -4

#a = calc_cube('5', 4) --> myTypeError --> '>' not supported between instances of 'str' and 'int'

#a = calc_cube(5, 4, h=2) --> a = calc_cube (5)
#                             a = calc_cube (4)
#                         raise ValueError(msg)
#                      ValueError: wrong val -2