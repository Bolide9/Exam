# Напишите программу калькулятор, которые принимает 2 числа и выполняет следующие операции: +, -, *, /.

a = int(input())
b = int(input())

symb = str(input('Введите символ: '))

if symb == '+':
    print(a + b)
if symb == '-':
    print(a - b)
if symb == '*':
    print(a * b)
if symb == '/':
    print(a / b)
