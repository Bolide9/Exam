'''
Напишите программу, которая рандомно генерирует 30 чисел находит те, которые делятся на 5 и найдите сумму этих чисел.
'''

import random

lst = []
_lst = []

for i in range(30):
    # Через random.random(), генерирует float включительно
    # Если нужно по условию - заменить строку ниже на:
    # lst.append(random.random())
    lst.append(random.randrange(1, 10000))

for i in lst:
    if i % 5 == 0: _lst.append(i)

print(_lst)
print(sum(_lst))