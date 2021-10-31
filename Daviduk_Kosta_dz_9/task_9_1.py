# task_9_1.py
# Создать класс TrafficLight (светофор).
# определить у него один атрибут __color - приватный
# и метод running - переключение светофора в режимы: красный - 7s, жёлтый - 2s, зелёный- 5s
# создать экземпляр и вызвать описанный метод

import time


class TrafficLight:
    colors_time = [('красный', 1), ('жёлтый', 1), ('зелёный', 1)]

    def __init__(self, __color: str, repeat_value):
        """
            режимы:'красный','жёлтый','зелёный'
            :param __color : цвет старта
            :param repeat_value: количество циклов
            :return:None
        """
        self.__color = __color
        self.repeat = repeat_value

    def running(self):
        for i in range(len(TrafficLight.colors_time)):
            TrafficLight.colors_time.insert(0, TrafficLight.colors_time.pop())
            if self.__color == TrafficLight.colors_time[0][0]:
                while self.repeat:
                    for j in range(len(TrafficLight.colors_time)):
                        time.sleep(TrafficLight.colors_time[j][1])
                        print(f'{TrafficLight.colors_time[j][0]}')
                    self.repeat -= 1
                exit()
        raise SyntaxError(f'SyntaxError: wrong word "{self.__color}":\n Введите режим светофора')


pedestrian = TrafficLight('жёлтый', 2)
try:
    pedestrian.running()
except SyntaxError as e:
    print(f'raise SyntaxError(msg)\n {e}')

# pedestrian = TrafficLight('жёлтый', 2)
# жёлтый
# зелёный
# красный
# жёлтый
# зелёный
# красный

# pedestrian = TrafficLight('оранжевый', 1)
# raise SyntaxError(msg)
#  SyntaxError: wrong word "оранжевый":
#  Введите режим светофора