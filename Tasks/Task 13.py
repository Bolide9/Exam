'''
Напишите программу: Вводится целое число. Вывести число, обратное введенному по порядку составляющих его цифр. Например, введено 3425, надо вывести 5243.
'''

a = int(input('Число: '))
print(str(a)[::-1])
