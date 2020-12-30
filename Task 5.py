# Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.

lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [2, 4, 6, 8]


def fun(_lst1, _lst2):
    res = list()
    for element in _lst1:
        if element not in _lst2:
            res.append(element)

    print(res)


fun(lst1, lst2)