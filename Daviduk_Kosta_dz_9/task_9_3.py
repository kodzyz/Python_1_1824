# task_9_3.py
#Реализовать базовый класс Worker
#атрибуты: name, surname, position, __income = {"wage": wage, "bonus": bonus}
#создать класс Position(Worker)
#реализовать методы:(get_full_name), (get_total_income)
#создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров

class Worker:
    def __init__(self, name, surname, position, __income):
        self.name = name
        self.surname = surname
        self.position = position
        for key in __income:
            setattr(self, key, __income[key])  # атрибуты в класс из словаря

class Position(Worker):
    def get_full_name(self):
        worker_info = dict(name=self.name, surname=self.surname, position=self.position, total_income=self.get_total_income())
        return ''.join(map(str, [worker_info]))

    def get_total_income(self):
        return self.wage + self.bonus


__income = {"wage": 800, "bonus": 100}

result = Position('Константин', 'Давидюк', 'инженер', __income)
print(f' полные данные сотрудника: {result.get_full_name()}')
print(f' доход с учётом премии: {result.get_total_income()}')
print(result.surname)
print(result.wage)

# полные данные сотрудника: {'name': 'Константин', 'surname': 'Давидюк', 'position': 'инженер', 'total_income': 900}
# доход с учётом премии: 900
# Давидюк
# 800