'''
Вычислить длину и площадь окружности при заданном радиусе. Значение радиуса вводится с клавиатуры
'''
import math

radius = int(input('Радиус: '))

len_cr = math.pi * 2 * radius

s_cr = math.pi * (radius * radius)

print('Длина окружности: ' + str(len_cr))
print('Площадь окружности: ' + str(s_cr))