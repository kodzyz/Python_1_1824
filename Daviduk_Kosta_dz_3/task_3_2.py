# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


def num_translate_adv(text: str):
    """перевод числительных от 0 до 10 c английского на русский язык c учетом заглавной буквы"""
    if text.istitle():
        d_z1 = dict(zip(['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'],
                   ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять', 'Десять']))
        print(d_z1.get(text, None))
    else:
        d_z = dict(zip(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],
                     ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']))
        print(d_z.get(text, None))


#per = (input('Введите :  '))
per = 'Два'

num_translate_adv(per)