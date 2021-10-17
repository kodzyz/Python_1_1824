# task_3.py
# Есть два списка:
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
#klasses = ['9А',   '7В',       '9Б',     '9В',    '8Б',      '10А',    '10Б',  '9А']
klasses = [ '9А',   '7В',       '9Б']

#
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>),
# например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# Доказать, что вы создали именно генератор.
# Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.
#


def para_walks(*args):
    """
    :param args: any number of lists
    :return: generating tuples
    """
    [klasses.append(None) for i in range(len(tutors) - len(klasses))]
    return zip(tutors, klasses) # ф-я zip итерируемый объект с.430 Марк Лутц


tup = para_walks(tutors, klasses)
print(next(tup)) #('Иван', '9А')
print(next(tup)) #('Анастасия', '7В')
print(next(tup)) #('Петр', '9Б')
print(next(tup)) #('Сергей', None)
print(next(tup)) #('Дмитрий', None)
print(next(tup)) #('Борис', None)
print(next(tup)) #('Елена', None)
#дальше истощение
print(next(tup))
#StopIteration


