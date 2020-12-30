"""Напишете функцию, которая принимает список и возвращает True, если все числа в последовательности уникальны,
в противном случае False.
"""

# Задаем список чисел
numbers = [3, 2, 4, 5, 7, 3, 10, 11, 12]


# Объявляем функцию
def check_uniqueness(numbers):
    # Способ 1
    # Проходимся циклом по всем элементам и смотрим количество вхождений в список данного элемента

    """
    for index in numbers:
        if(numbers.count(index) > 1):
            return print(f'True {index}')
        else:
            print('False')
    """

    # Способ 2
    # Функция set - возвращает уникальные элемента в виде множества
    # С помощью функции set возвращаем уникальные элементы и сравниваем длину уникального списка с исходным
    set_numbers = set(numbers)
    if len(set_numbers) == len(numbers):
        return print(f'True')
    else:
        return print(f'False')


# Вызываем функцию
check_uniqueness(numbers)
