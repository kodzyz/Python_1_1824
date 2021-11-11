#task_11_5.py
# Продолжить предыдущее задание.
# Разработать методы - приём оргтехники на склад
# и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).

from abc import ABC, abstractmethod

class Material_values(ABC):
    @abstractmethod
    def device_info(self):
        pass

class Store:
    def __init__(self, org): #тип имущества - "Оргтехника", инвентарный номер - "00000001(не реализовал)"
        self.org = org
        self.store_list = []
        self.amount = 0
    def __str__(self):
        return f'Перечень оргтехники на складе: "{self.store_list}" в количестве {self.device_amount()} шт.'
    def store_metod(self):
        self.store_list.append(self.org.device_remove())
        return self.store_list
    def device_amount(self):
        self.amount = len(self.store_list)
        return self.amount

class OfficeEquip(Material_values):                       #"Оргтехника в компании" : имя
    typical_properties = ['тип', 'разрешение', 'формат', 'дисплей'] # общие свойства для оргтехники
    def __init__(self, name):
        self.name = name
        self.list_device = []  # список 'имен' всей техники(экземпляров)
        self. amount = 0
    def device_info(self, device):
        for i in device.device_info():
            self.list_device.append(i)
        return self.list_device
    def __str__(self):
        return f'Перечень оргтехники в компании "{self.name}":\n {self.list_device} в количестве {self.device_amount()} шт.'
    def device_amount(self):
        self.amount = len(self.list_device)
        return self.amount
    def device_remove(self):
        return self.list_device.pop()
    @staticmethod
    def info(name, args):
        equip_name = name
        name_feature_dict = {}
        properties = OfficeEquip.typical_properties
        feature_list = args
        feature_dict = dict(zip(properties, feature_list))
        name_feature_dict.setdefault(equip_name, feature_dict)
        return name_feature_dict

class Printer(OfficeEquip):                     # (лазерные, струйные), (A0, A1, A2, A3, A4, A6)
    #special_properties = ['скорость'] # далее расширить дополнительныим свойствами(не реализовал)
    def __init__(self, name, *args):
        super().__init__(name)
        self.character = args
        self.list_info = self.device_info()
    def device_info(self):
        return self.info(self.name, self.character)

class Scanner(OfficeEquip):                     # разрешение, глубина цвета
    #special_properties = ['глубина'](не реализовал)
    def __init__(self, name, *args):
        super().__init__(name)
        self.character = args
        self.list_info = self.device_info()
    def device_info(self):
        return self.info(self.name, self.character)

class Xerox(OfficeEquip):                         # разрешение
    def __init__(self, name, *args):
        super().__init__(name)
        self.character = args
        self.list_info = self.device_info()
    def device_info(self):
        return self.info(self.name, self.character)


printer_1 = Printer('Canon PIXMA MG2540S', 'лазерный', '1200x1200', 'А4', 'да')
scanner_1 = Scanner('Epson Perfection V19', 'планшетный', '1200x600', 'А4', 'нет')
xerox_1 = Xerox('Xerox B215', 'настольный', '1200x2400', 'А3', 'нет')
xerox_2 = Xerox('Xerox 3020', 'портативный', '1200x1200', 'А4', 'нет')
print('\n"Оргтехника" - имя и параметры:')
print(printer_1.device_info())
print(scanner_1.device_info())
print(xerox_1.device_info())
print(xerox_2.device_info())
print('\n"Оргтехника" в офисе:')
our_technique = OfficeEquip('WITTOCHPRIBOR') # вся техинка в компании 'WITTOCHPRIBOR'
for obj in (printer_1, scanner_1, xerox_1, xerox_2):
    our_technique.device_info(obj)
print(our_technique)
print('\n"Оргтехника" на складе:')
store = Store(our_technique)
print(store)
print()
store.store_metod()
print('"Оргтехника" после передачи на склад:\n')
print(our_technique)
print()
print(store)

# "Оргтехника" - имя и параметры:
# {'Canon PIXMA MG2540S': {'тип': 'лазерный', 'разрешение': '1200x1200', 'формат': 'А4', 'дисплей': 'да'}}
# {'Epson Perfection V19': {'тип': 'планшетный', 'разрешение': '1200x600', 'формат': 'А4', 'дисплей': 'нет'}}
# {'Xerox B215': {'тип': 'настольный', 'разрешение': '1200x2400', 'формат': 'А3', 'дисплей': 'нет'}}
# {'Xerox 3020': {'тип': 'портативный', 'разрешение': '1200x1200', 'формат': 'А4', 'дисплей': 'нет'}}
#
# "Оргтехника" в офисе:
# Перечень оргтехники в компании "WITTOCHPRIBOR":
#  ['Canon PIXMA MG2540S', 'Epson Perfection V19', 'Xerox B215', 'Xerox 3020'] в количестве 4 шт.
#
# "Оргтехника" на складе:
# Перечень оргтехники на складе: "[]" в количестве 0 шт.
#
# "Оргтехника" после передачи на склад:
#
# Перечень оргтехники в компании "WITTOCHPRIBOR":
#  ['Canon PIXMA MG2540S', 'Epson Perfection V19', 'Xerox B215'] в количестве 3 шт.
#
# Перечень оргтехники на складе: "['Xerox 3020']" в количестве 1 шт.