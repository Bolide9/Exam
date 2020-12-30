'''
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере – входные
данные: 6, выходные данные: The next number for the number 6 is 7. The previous number for the number 6 is 5.
'''

for i in range(1,100):
    print(f'The next number for the number {i} is {i+1}\nThe previous number for the number {i} is {i-1}\n')