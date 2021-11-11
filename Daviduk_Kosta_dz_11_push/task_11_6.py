#task_11_6.py
# Продолжить работу над предыдущим заданием.
# Реализовать механизм валидации вводимых пользователем данных.
'''проверку входных значений осуществляю c помощью геттер/сеттер'''

from abc import ABC, abstractmethod

class MPMCatErr(Exception):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return f'My_Personal_Method_of_Catching_Errors: "{self.text}"\n ' \
               f'typical_properties = ["тип", "разрешение", "формат", "дисплей"]\n' \
               f'или расширте список допустимых свойств!'

class Material_values(ABC):
    @abstractmethod
    def device_info(self):
        pass

class Store:
    def __init__(self, org):
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

class OfficeEquip(Material_values):
    typical_properties = ['тип', 'разрешение', 'формат', 'дисплей']
    def __init__(self, name):
        self.name = name
        self.list_device = []
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

class Printer(OfficeEquip):
    def __init__(self, name, *args):
        super().__init__(name)
        self.character = args
        self.list_info = self.device_info()
    def device_info(self):
        return self.info(self.name, self.character)
    @property
    def args(self):
        return self.character
    @args.setter
    def args(self, a):
        if len(a) == len(OfficeEquip.typical_properties):
            self.character = a
        else:
            raise MPMCatErr(f'{a}')

class Scanner(OfficeEquip):
    def __init__(self, name, *args):
        super().__init__(name)
        self.character = args
        self.list_info = self.device_info()
    def device_info(self):
        return self.info(self.name, self.character)

    @property
    def args(self):
        return self.character
    @args.setter
    def args(self, a):
        if len(a) == len(OfficeEquip.typical_properties):
            self.character = a
        else:
            raise MPMCatErr(f'{a}')

class Xerox(OfficeEquip):
    def __init__(self, name, *args):
        super().__init__(name)
        self.character = args
        self.list_info = self.device_info()
    def device_info(self):
        return self.info(self.name, self.character)
    @property
    def args(self):
        return self.character
    @args.setter
    def args(self, a):
        if len(a) == len(OfficeEquip.typical_properties):
            self.character = a
        else:
            raise MPMCatErr(f'{a}')


printer_1 = Printer('Canon PIXMA MG2540S', 'лазерный', '1200x1200', 'А4', 'да', '8')
try:
    printer_1.args = ('Canon PIXMA MG2540S', 'лазерный')
except MPMCatErr as e:
    print(e)

# My_Personal_Method_of_Catching_Errors: "()"
#  typical_properties = ["тип", "разрешение", "формат", "дисплей"]
# или расширте список допустимых свойств!

