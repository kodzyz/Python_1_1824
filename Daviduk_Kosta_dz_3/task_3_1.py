# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

# Mark Lutz# c.147 #zip Создание словаря bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))


def num_translate(text: str):
    """перевод числительных от 0 до 10 c английского на русский язык"""
    d_z = dict(zip(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],
                   ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']))
    print(d_z.get(text, None))


#per = (input('Введите :  '))
per = 'one'
num_translate(per)