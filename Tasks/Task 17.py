'''
Напишите программу: Из списка чисел удалить элементы, значения которых больше 35. При этом удаляемые числа сохранить в другом списке.
'''

import random

lst = []
_lst = []

for i in range(10):
    lst.append(random.randrange(1, 100))

print(lst)

i = 0
while i < len(lst):
    if lst[i] > 35:
        _lst.append(lst[i])
        del lst[i]
    else:
        i += 1

print(lst)
print(_lst)
