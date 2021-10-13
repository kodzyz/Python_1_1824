#5. * (вместо 4)
# Доработать скрипт из предыдущего задания:
# теперь он должен работать и из консоли.

from utils import currency_rates_adv

def main_adv(argv):
   program, *code = argv
   cod_up = ''.join(code).upper()
   curren, dat = currency_rates_adv(cod_up)
   print(f'1 {cod_up} = {curren} RUB на {dat.day}.{dat.month}.{dat.year} г.')
   return 0


if __name__ == '__main__':
   import sys

   exit(main_adv(sys.argv))

# PS C:\PyProjects\Python_1_1824\Daviduk_Kosta_dz_4> python task_4_5.py EUR
# 1 EUR = 83.0028 RUB на 14.10.2021 г.