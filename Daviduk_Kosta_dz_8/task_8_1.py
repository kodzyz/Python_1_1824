# task_8_1.py

#def email_parse(<email_address>), которая при помощи regular expressions
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.
# Пример:

# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}

# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

# Примечание:
# подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re
RE_MAIL_PARS = re.compile(r'(?P<username>[a-z0-9\.\-+_]+)@(?P<domain>[a-z0-9\.\-+_]+\.[a-z]+)')


def email_parse(email):
    if RE_MAIL_PARS.match(email):
        m = re.match(RE_MAIL_PARS, email)
        print(m.groupdict())
    else:
        raise ValueError(f'ValueError: wrong email:{email}')
    return


try:
    email_parse('someone@geekbrains.ru')
except ValueError as e:
    print(f'raise ValueError(msg)\n {e}')