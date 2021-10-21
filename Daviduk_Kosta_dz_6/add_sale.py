#task_6_6 : для записи данных
# -из командной строки значение суммы продаж
# Примеры запуска скриптов:
#  python add_sale.py 5978,5
#  python add_sale.py 8914,3


def enter_fun(argv):
    program, *arg = argv
    arg_st = ','.join(arg)
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{arg_st}\n')


if __name__ == '__main__':
    import sys
    exit(enter_fun(sys.argv))
