# task_8_3.py

#Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>

# Примечание: если аргументов несколько - выводить данные о каждом через запятую
#можете ли вы вывести тип значения функции?
#Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
#Сможете ли вывести имя функции, например, в виде:

# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'> )

def type_logger(func):
    def tag_wrapper(*args, **kwargs):
        for i in args:
            print(f'{func.__name__}({i}: {type(i)})')
        for i in kwargs.values():
            print(f'{func.__name__}({i}: {type(i)})')
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

@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5, 15, h=2, g=3.3)
print(a)
# calc_cube(5: <class 'int'>)
# calc_cube(15: <class 'int'>)
# calc_cube(2: <class 'int'>)
# calc_cube(3.3: <class 'float'>)
# 125, 3375, 8, 35.937


# a = calc_cube(5, '15', h=2, g=3.3)
# print(a)
# calc_cube(5: <class 'int'>)
# calc_cube(15: <class 'str'>)
# calc_cube(2: <class 'int'>)
# calc_cube(3.3: <class 'float'>)
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
#  "To get the result, enter integers"
# None

