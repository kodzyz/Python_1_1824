#3. * (вместо 2) Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?

import requests
import datetime
from cbr_parser.utils import extract_data


def currency_rates_adv(char_code: str):
    """
    аргумент -  код валюты
    return - курс этой валюты, дату
    """
    r = requests.post('http://www.cbr.ru/scripts/XML_daily.asp')
    string = r.text
    s = ''.join(i for i in string if i.isalnum())  # if i = True
    new_s = ''
    for i in range(len(s)):
        if s[i].isdigit():
            new_s += s[i]
            if s[i + 1].isdigit() == 0 and len(new_s) != 8:
                new_s = ''
            elif s[i + 1].isdigit() == 0 and len(new_s) == 8:
                break
    date = datetime.date(int(new_s[4:]), int(new_s[2:4]), int(new_s[:2]))

    code_valut = extract_data('CharCode')
    value_valutes = extract_data('Value')
    val_float = [(x.replace(',','.')) for x in value_valutes]
    val = [float(x.strip('"')) for x in val_float]
    d_v = dict(zip(code_valut, val))
    _ch = char_code.upper()
    rate = d_v.get(_ch)
    return  rate, date


#per = (input('Введите код валюты:   '))
code = 'bYn'

cod_up = code.upper()
curren, dat = currency_rates_adv(code)
print(type(curren))
print(type(dat))
print(f'1 {cod_up} = {curren} RUB на {dat.day}.{dat.month}.{dat.year} г.')

