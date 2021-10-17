import sys
from time import perf_counter
#task_5.py
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка
# их следования в исходном списке,
# например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.


# Лучше, чем решено в методичке я и не придумал! Остается только посмотреть по скоростям и объему
def un_src(args):
    return [i for i in args if args.count(i) == 1]


def un_src_adv(args):
    return (i for i in args if args.count(i) == 1)


def un_src_adv1(args):
    unique_src = set()
    tmp = set()
    for el in args:
        if el not in tmp:
            unique_src.add(el)
        else:
            unique_src.discard(el)
        tmp.add(el)
    unique_src_ord = [el for el in args if el in unique_src]
    yield unique_src_ord


start = perf_counter()
print(type(un_src(src)), un_src(src), sys.getsizeof(un_src(src)), perf_counter() - start)
#<class 'list'> [23, 1, 3, 10, 4, 11] 128 2.7095386846174974e-05
start = perf_counter()
print(type(un_src_adv(src)), list(un_src_adv(src)), sys.getsizeof(un_src_adv(src)), perf_counter() - start)
#<class 'generator'> [23, 1, 3, 10, 4, 11] 88 3.7358790954574586e-05

start = perf_counter()
print(type(un_src_adv1(src)), *un_src_adv1(src), sys.getsizeof(un_src_adv1(src)), perf_counter() - start)
#<class 'generator'> [23, 1, 3, 10, 4, 11] 88 8.867581149657264e-05