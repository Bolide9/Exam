'''
Напишите программу: Дана строка, содержащая натуральные числа и слова. Необходимо сформировать список из чисел,
содержащихся в этой строке. Например, задана строка "abc83 cde7 1 b 24". На выходе мы должны получить список [83, 7, 1, 24].
'''

import re

string = 'abc83 cd5445e7 1 b54654dsadas56 ^&&^$&$*(24)dadfsjnad'
_string = string.strip()

nums = re.findall(r'\d+', _string)
nums = [i for i in nums if i.isdigit()]

print(nums)
