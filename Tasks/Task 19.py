'''
Напишите функцию, которая на вход получает строку – ФИО человека и возвращает сокращенный вариант записи ФИО.
Например, вводим: Иванов Иван Петрович, в результате должны получить: Иванов И. П.
'''

string = str(input('Введите ФИО: '))


def get_initial(_string):
    val = _string.split()
    print(f'{val[0]} {str(val[1][:1]).upper()}. {str(val[2][:1]).upper()}.')


get_initial(string)
