'''
Напишите функцию, которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два.
'''

lst = []


def func(_lst):
    while len(_lst) != 5:
        _lst.append(int(input('Введите число: ')))

    # через enumerate почему-то не работает
    # питухон +
    for i in range(len(_lst)-1,-1,-1):
        if _lst[i] % 2 == 0:
            _lst[i] //= 2
        else:
            _lst.pop(i)

    print(_lst)


func(lst)
