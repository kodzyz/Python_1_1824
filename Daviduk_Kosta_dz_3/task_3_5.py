#get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):

#Сможете ли вы добавить еще один аргумент —
# флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

nouns =      ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs =    ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

#         	Например:
# >>> get_jokes(2)
#["лес завтра зеленый", "город вчера веселый"]


import random


def get_jokes(per, f='1', **kwargs):

    if f == '0' and int(per) <= 5: # шутки без повтора и их меньше(равно) чем 5
        d_z = dict(zip(['1', '2', '3', '4', '5'], [4, 3, 2, 1, 0]))
        x = d_z.get(per, 5)
        random.shuffle(nouns)  # смещение списков от 0 до 5 шагов - не дает повтора (исхожу и этого)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        for n in range(len(nouns) - x):
            print(f'{nouns[n]} {adverbs[n]} {adjectives[n]}')
    elif f == '0' and int(per) > 5: # максимальное кол. шуток без повтора =5
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        for n in range(5):
            print(f'{nouns[n]} {adverbs[n]} {adjectives[n]}')
    else:                           # шутки с повтором любое количество
        for n in range(int(per)):
            idx_n = nouns[random.randrange(len(nouns))]  # эта функция часто повторяется
            idx_adv = adverbs[random.randrange(len(adverbs))]
            idx_adje = adjectives[random.randrange(len(adjectives))]
            print(f'{idx_n} {idx_adv} {idx_adje}')


#amount = (input('Введите кол(0-n) шуток:  '))
amount = '4' # количество шуток

allow_flag = '0'  # 0 - запрет на повторы # 1 - разрешение на повторы

get_jokes(amount, f=allow_flag, n=nouns, adv=adverbs, adj=adjectives)