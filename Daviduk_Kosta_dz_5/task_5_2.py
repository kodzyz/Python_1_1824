# task_2.py
# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n
# (включительно),
# не используя ключевое слово yield.
#

#Вариант1
def odd_nums_adv(n):
    num_odd = (i for i in range(1, n + 1, 2))
    return num_odd


odd_to_15 = odd_nums_adv(15)
# for i in odd_to_15:
#     print(i, end=' ')

print(next(odd_to_15))
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
print(next(odd_to_15))

next(odd_to_15)
#тут - StopIteration


# #Вариант2 с.611 Марк Лутц
# def odd_nums_adv2(n):
#     for x in map((lambda n: n), range(1, n + 1, 2)):
#         print(x, end=' : ') #1 : 3 : 5 : 7 : 9 : 11 : 13 : 15 :
#
#
# odd_to_15 = odd_nums_adv2(15)
