import sys
from time import perf_counter
#task_4.py
# Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
#
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

def more_prev(args):
    res = []
    for i in range(len(args) - 1):
        if src[i] < src[i + 1]:
            res.append(src[i + 1])
    return res

def more_prev1(args):
    res = []
    for i in range(len(args) - 1):
        if src[i] < src[i + 1]:
            res.append(src[i + 1])
    yield res


def more_prev2(args):
    return (src[i + 1] for i in range(len(args) - 1) if src[i] < src[i + 1])


def more_prev3(args):
    return (j for i, j in zip(args, args[1:]) if j > i)


start = perf_counter()
result = more_prev(src)
print(type(result), result, sys.getsizeof(result), perf_counter() - start)
#<class 'list'> [12, 44, 4, 10, 78, 123] 128 1.5189956564935012e-05

start = perf_counter()
result1 = more_prev1(src)
print(type(result1), *result1, sys.getsizeof(result1), perf_counter() - start)
#<class 'generator'> [12, 44, 4, 10, 78, 123] 88 9.852944798876765e-06

start = perf_counter()
result2 = more_prev2(src)
print(type(result2), list(result2), sys.getsizeof(result2), perf_counter() - start)
#<class 'generator'> [12, 44, 4, 10, 78, 123] 88 1.5600495931554876e-05
#
start = perf_counter()
result3 = more_prev3(src)
print(type(result3), list(result3), sys.getsizeof(result3), perf_counter() - start)
# <class 'generator'> [12, 44, 4, 10, 78, 123] 88 1.8063732131274066e-05