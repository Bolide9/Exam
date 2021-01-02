'''
Вычислить площадь треугольника по трем сторонам – a, b, c. Длины сторон ввести с клавиатуры.
'''
import math

a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

p = (a + b + c) / 2
c = p * (p-a) * (p-b) * (p-c)
s = math.sqrt(c)

print(f'{s} м2')