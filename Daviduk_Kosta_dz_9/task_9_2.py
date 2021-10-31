# task_9_2.py
# Реализовать класс Road
# определить атрибуты: _length, _width - должны передаваться при создании экземпляра
# метод расчёта массы асфальта = _length * _width * 25 кг * 5 см = 12500 т.
#, uint='м'
#self.uint = uint
class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return (self._length * self._width * 25 * 5)/1000

highway = Road(20, 5000)
print('%0d т.' % highway.mass())

#12500 т.