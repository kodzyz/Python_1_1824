#task_11_4.py
# Создать класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым( определить общие параметры)
# для классов-наследников: типы оргтехники (принтер, сканер, ксерокс)
# реализовать параметры, уникальные для каждого типа оргтехники.

class Store:
    def __init__(self, type_stuff, inv_num): #тип имущества - "Оргтехника", инвентарный номер - "00000001"
        self.type_prop = type_stuff
        self.inv_num = inv_num
    def __str__(self):
        return f'{self.type_prop} : {self.inv_num}'

class OfficeEquip:                       #"Оргтехника": имя
    def __init__(self, name):
        self.name = name
    def my_list(self):
        pass

class Printer(OfficeEquip):                     # (лазерные, струйные), (A0, A1, A2, A3, A4, A6)
    def __init__(self, name, type, paper_size):
        super().__init__(name)
        self.type = type
        self.paper_size = paper_size

class Scanner(OfficeEquip):                     # разрешение, глубина цвета
    def __init__(self, name, resolution, bit):
        super().__init__(name)
        self.resolution = resolution
        self.bit = bit

class Xerox(OfficeEquip):                         # разрешение
    def __init__(self, name, dpi):
        super().__init__(name)
        self.dpi = dpi




