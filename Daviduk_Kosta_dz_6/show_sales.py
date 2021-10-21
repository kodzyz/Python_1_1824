#task_6_6 : Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить ис номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить с номера, равного первому числу, по второе число, включительно.
# Примеры запуска скриптов:
# python show_sales.py
# python show_sales.py 3
# python show_sales.py 1 3

def recap_fun(argv):
    program, *arg = argv
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if (len(sys.argv)-1) == 0:
            lines = f.readlines()
            for i in range(len(lines)):
                print(f'{str(i + 1)} : {lines[i].strip()}')
        elif (len(sys.argv)-1) == 1:
            lines = f.readlines()
            start = int(''.join(arg[0]))
            for i in range(start - 1, len(lines)):
                print(f'{str(i + 1)} : {lines[i].strip()}')
        elif (len(sys.argv)-1) == 2:
            lines = f.readlines()
            start = int(''.join(arg[0]))
            end = int(''.join(arg[1]))
            if end <= len(lines):
                for i in range(start - 1, end):
                    print(f'{str(i + 1)} : {lines[i].strip()}')
            else:
                for i in range(start - 1, len(lines)):
                    print(f'{str(i + 1)} : {lines[i].strip()}')



if __name__ == '__main__':
    import sys
    exit(recap_fun(sys.argv))
