import requests
import datetime
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

    return rate


def currency_rates_adv(char_code: str):
    """
    аргумент -  код валюты
    return - курс этой валюты, дату
    """
    r = requests.post('http://www.cbr.ru/scripts/XML_daily.asp')
    string = r.text
    s = ''.join(i for i in string if i.isalnum())
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