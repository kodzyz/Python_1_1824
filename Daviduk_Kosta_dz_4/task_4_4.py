#4. Написать свой модуль utils и перенести в него функцию currency_rates()
# из предыдущего задания. Создать скрипт, в котором импортировать этот модуль и
# выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

from utils import currency_rates



name = 'BYN'
print(f'1 {name}  = {currency_rates(name)} RUB')
name = 'AUD'
print(f'1 {name}  = {currency_rates(name)} RUB')
name = 'CNY'
print(f'1 {name}  = {currency_rates(name)} RUB')
name = 'UAH'
print(f'1 {name}  = {currency_rates(name)} RUB')
