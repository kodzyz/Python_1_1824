# task_11_3.py
# Создать собственный класс-исключение,
# пользователь может вводить только числа или строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться
# пока пользователь сам не остановит работу скрипта, введя, например, команду «stop»

from decimal import Decimal
import re

class MyValueError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'MyValueError: "{self.text}", waiting for the number'


re_data = re.compile(r'[+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?')
only_float = []
while True:
    every = input('Enter value :  ')
    if every == 'stop':
        break
    try:
        if every == '0':
            every = '0.0'
        if re_data.match(every) or every == '0':
            every = float(every.replace(',', '.').lstrip('0'))
            only_float.append(every)
        else:
            raise MyValueError(f'{every}')
    except ValueError:
        print('Error type of value!')
    except MyValueError as e:
        print(e)
        continue
only_float = map(str, only_float)
str_list = []
for i in only_float:
    if float(i) == 0.0:
        i = '0'
        str_list.append(i)
        continue
    while i[-1] == '0':
        i = i[:-1]
        if i[-1] == '.':
            i = i[:-1]
            break
    str_list.append(i)
print(str_list)

# Enter value :  0
# Enter value :  -0
# Enter value :  0.0
# Enter value :  -0.0000
# Enter value :  0.0
# Enter value :  00.0
# Enter value :  -00.000
# Enter value :  800
# Enter value :  900.000
# Enter value :  0.566
# Enter value :  -56
# Enter value :  5uuiui
# Error type of value!
# Enter value :  k6666
# MyValueError: "k6666", waiting for the number
# Enter value :  s
# ['0', '0', '0', '0', '0', '0', '0', '800', '900', '0.566', '-56']