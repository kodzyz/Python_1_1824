#task_7_3

# 1. - Создать структуру файлов и папок, при помощи скрипта
# |--my_project_7_3
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html

import os
import shutil
from my_exceptions import FuncAttributeFailError


def mk_fun(dict, path, suff='py', flag='w', folder='None'):
    '''
    :param dict: {'folder1':[filename,...], 'folder2': [...], ... }
    :param path: the path of the destination file or directory
    :param suff: file extension
    :param flag: flag='w' - write/ flag='с' - copy
    :param folder: only in mode 'copy' - destination copy file or directory
    :return: None
    '''
    for i in dict:
        starter = os.path.join(path, i)
        os.makedirs(starter, exist_ok=True)
        for j in dict[i]:
            if flag == 'w':
                with open(os.path.join(starter, f'{j}.{suff}'), 'w') as f:
                    f.write('')
            elif flag == 'c':
                g = os.path.join(starter, f'{j}.{suff}')
                shutil.copy2(g, folder)
            elif flag != 'c':
                raise FuncAttributeFailError(f'{flag} = c')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
comm_dir = os.path.join(BASE_DIR, 'my_project_7_3')
sub_dir = {'settings' : ['__init__', ' dev', 'prod'],
           'mainapp' : ['__init__', 'models', 'views'],
           'authapp' : ['__init__', 'models', 'views'] }

comm_dir2 = os.path.join(BASE_DIR, 'my_project_7_3\\mainapp\\templates')
sub_dir2 = {'mainapp' : ['base', 'index']}

comm_dir3 = os.path.join(BASE_DIR, 'my_project_7_3\\authapp\\templates')
sub_dir3 = {'authapp' : ['base', 'index']}
try:
    mk_fun(sub_dir, comm_dir)
    mk_fun(sub_dir2, comm_dir2, 'html')
    mk_fun(sub_dir3, comm_dir3, 'html')
except (TypeError, SyntaxError, NameError) as e:
    print(f'concrete error mk_fun(): {e}')
except OSError as e:
    print(f'global error mk_fun(): {e}')

# 2. - Написать скрипт, который собирает все шаблоны в одну папку 'templates'
# |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html

copy_dir = os.path.join(BASE_DIR, 'my_project_7_3\\templates')
copy_dir1 = os.path.join(BASE_DIR, 'my_project_7_3\\templates\\mainapp')
copy_dir2 = os.path.join(BASE_DIR, 'my_project_7_3\\templates\\authapp')

sub_copy = ['mainapp', 'authapp']
for i in sub_copy:
    folder = os.path.join(copy_dir, i)
    try:
        os.makedirs(folder)
    except FileExistsError as e:
        print(f'makedirs error: {e}')
        break

try:
    mk_fun(sub_dir2, comm_dir2, 'html', 'c', copy_dir1)
    mk_fun(sub_dir3, comm_dir3, 'html', 'c', copy_dir2)
except (TypeError, SyntaxError, NameError) as e:
    print(f'concrete error mk_fun(): {e}')
except OSError as e:
    print(f'global error mk_fun(): {e}')
except FuncAttributeFailError as e:
    print(f'FuncAttributeFailError: {e}')


print('end')

