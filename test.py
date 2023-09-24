from cstm_api import CsgotmApi
import time

api = CsgotmApi('')

with open('sum.txt', 'a', encoding='utf-8') as f:
    clock = time.strftime('%H:%M %d/%m')
    summa = api.check_sum(api.get_inventory())
    f.write(f'\n{clock} {summa}')
    print('Скрипт завершил работу!')
    
