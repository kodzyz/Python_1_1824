#1 Создать список, содержащий цены на товары

# if разскоментить  стороки (4 - 9) то закоментить строку (14) и наоборот

import random
com_prices = []
for i in range(0, 10):
    com_prices.append(random.randrange(10000)/100)
print(com_prices)
#[32.77, 5.61, 17.35, 66.18, 26.99, 76.69, 27.52, 51.01, 15.58, 41.02]

#2 Вывести на экран эти цены через запятую в одну строку «5 руб 04 коп», 07 коп

#3 Вывести цены, отсортированные по возрастанию, новый список не создавать

print(id(com_prices)) #39183496
com_prices.sort()
print(id(com_prices), com_prices) #39183496 [5.61, 15.58, 17.35, 26.99, 27.52, 32.77, 41.02, 51.01, 66.18, 76.69]

for cost in com_prices:
     pen_cost = cost % 1
     ru_cost = cost - pen_cost
     if pen_cost *100 <= 9:
         print(f'"{int(ru_cost)} руб 0{pen_cost * 100:.0f} коп",', end=' ')
     else:
         print(f'"{int(ru_cost)} руб {pen_cost*100:.0f} коп",', end=' ')

#"5 руб 61 коп", "15 руб 58 коп", "17 руб 35 коп", "26 руб 99 коп", "27 руб 52 коп", "32 руб 77 коп", "41 руб 02 коп", "51 руб 01 коп", "66 руб 18 коп", "76 руб 69 коп", .

#4 Создать новый список, содержащий те же цены, но отсортированные по убыванию.

print('.')
com_prices_reverd = list(reversed(com_prices))
print(id(com_prices_reverd), com_prices_reverd) #39225544 [76.69, 66.18, 51.01, 41.02, 32.77, 27.52, 26.99, 17.35, 15.58, 5.61]

#5 Вывести цены пяти самых дорогих товаров по возрастанию
_ = []
while len(com_prices_reverd) >= 6:
    i = len(com_prices_reverd)
    _.append(com_prices_reverd.pop(i-1))
print(com_prices_reverd) #[76.69, 66.18, 51.01, 41.02, 32.77]
mo_exp = list(reversed(com_prices_reverd))
print(mo_exp) #[32.77, 41.02, 51.01, 66.18, 76.69]
for cost in mo_exp:
     pen_cost = cost % 1
     ru_cost = cost - pen_cost
     if pen_cost *100 <= 9:
         print(f'"{int(ru_cost)} руб 0{pen_cost * 100:.0f} коп",', end=' ')
     else:
         print(f'"{int(ru_cost)} руб {pen_cost*100:.0f} коп",', end=' ')

#"32 руб 77 коп", "41 руб 02 коп", "51 руб 01 коп", "66 руб 18 коп", "76 руб 69 коп",