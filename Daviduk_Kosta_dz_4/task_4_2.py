#2. Написать функцию currency_rates(),
# принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере,
# посмотреть содержимое ответа. Можно ли, используя только методы класса str,
# решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.

from cbr_parser.utils import extract_data


def currency_rates(char_code: str) -> float:
    """
    аргумент -  код валюты
    return - курс этой валюты
    """
    code_valut = extract_data('CharCode')
    value_valutes = extract_data('Value')

    val_float = [(x.replace(',','.')) for x in value_valutes]
    val = [float(x.strip('"')) for x in val_float] # как не крутил через filter map lambda - не получилось

    d_v = dict(zip(code_valut, val))

    _ch = char_code.upper()
    rate = d_v.get(_ch)

    return  rate


#per = (input('Введите код валюты:   '))
code = 'eUr'

_c = code.upper()
curren = currency_rates(code)
print(type(curren))
print(f'1 {_c} = {curren} RUB')

