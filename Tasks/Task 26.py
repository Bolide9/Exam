'''
Напишите программу, на вход подается строка, если в строке присутствуют цифры,
необходимо их извлечь, подсчитать сумму квадратов этих чисел, если же в строке нет цифр вывести «В данной строке нет цифр».
'''

import re

string = input('Ввод условной строки: ')
_string = string.strip()

nums = re.findall(r'\d+', _string)
nums = [i for i in nums if i.isdigit()]

if len(nums) != 0:
    for i in nums:
        print(int(i) * int(i))
else:
    print('В данной строке нет цифр')
