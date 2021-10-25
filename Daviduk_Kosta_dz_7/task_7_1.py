#task_7_1
import os
# |--my_project_7_1
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
comm_dir = os.path.join(BASE_DIR, 'my_project_7_1')
sub_dir = ['settings', 'mainapp', 'adminapp', 'authapp']
for i in sub_dir:
    starter = os.path.join(comm_dir, i)
    os.makedirs(starter, exist_ok=True)
print('end')
