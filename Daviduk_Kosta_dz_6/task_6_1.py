#1
# Не используя библиотеки для парсинга, распарсить
# (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
# Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]

import json


def sempl_list(fl):
    """
    :param dat: txt
    :return: [('...', '...', '...'), ('...', '...', '...')]
    """
    a = []
    b = []
    c = []
    for i in fl:
        u = i.split(' ')
        a.append(u[0])
        b.append(u[5].strip('"'))
        c.append(u[6])
        #d = zip(a, b, c)
    return list(zip(a, b, c)) #[('93.180.71.3', 'GET', '/downloads/product_1')] при i = 0



with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    smple = sempl_list(f)
    d_str = json.dumps(smple) #encoder

# если так: d = zip(a, b, c)
#то:
# print(next(smple)) #('93.180.71.3', 'GET', '/downloads/product_1')
# print(next(smple)) #('93.180.71.3', 'GET', '/downloads/product_1')
# print(next(smple)) #('80.91.33.133', 'GET', '/downloads/product_1')

#для проверки создал файл nginx_out.txt
with open('nginx_out.txt', 'w+', encoding='utf-8') as f:
    f.write(d_str)
#[
# ["93.180.71.3", "GET", "/downloads/product_1"],
# ["93.180.71.3", "GET", "/downloads/product_1"],
# ["80.91.33.133", "GET", "/downloads/product_1"],
#...]

# тут странность - в файле списки в списке?!!!
# глюк перевода?
# в таблице соответствий тип "tuples" не значится


