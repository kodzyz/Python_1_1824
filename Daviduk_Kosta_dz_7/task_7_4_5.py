# task_7_4. task_7_5.

# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

# task_7_5
# {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
#Сохраните результаты в файл <folder_name>_summary.json в той же папке,
# где запустили скрипт. (task_7_5_summary.json)


from task_7_1 import BASE_DIR, os
from collections import defaultdict
import django
import json # для набора каталогов и файлов установил фреймворк Django ->см.'requirements.txt'


def compare(bulk):
        num = [10 ** n for n in range(1, 100)]
        for i in num:
                if 0 <= bulk <= i:
                        return i


#comm_dir = django.__path__[0]
#comm_dir = os.path.join(BASE_DIR, 'some_data')
#comm_dir = os.path.join(BASE_DIR, 'my_project_7_3')
comm_dir = BASE_DIR #'C:\\PyProjects\\Python_1_1824\\Daviduk_Kosta_dz_7'


dz_7_files = defaultdict(list)
# обыграл задачку в методичке,- 'спасибо ей за это'

for root, dirs, files in os.walk(comm_dir):
        for f in files:
                fp = os.path.join(root, f)
                size = os.stat(fp).st_size
                ext = f.rsplit('.', maxsplit=1)[-1].lower()
                dz_7_files[compare(size)].append(ext)

# task_7_4
my = {ext : (len(files)) for ext, files in sorted(dz_7_files.items())}
print(f'Результ к задаче task_7_4: \n{my}')
print()
# task_7_5
by = {ext : (len(files), list(set(files))) for ext, files in sorted(dz_7_files.items())}
print(f'Результ к задаче task_7_5: \n{by}')

by_as_str = json.dumps(by)
with open('task_7_5_summary.json', 'w', encoding='utf-8') as f:
        f.write(by_as_str)


print('end')