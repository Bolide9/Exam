'''
Напишите программу: В строке заменить пробелы звездочкой. Если встречается подряд несколько пробелов,
то их следует заменить одним знаком "*", пробелы в начале и конце строки удалить
'''

string = 'Напишите программу: В строке заменить пробелы звездочкой.   Если встречается подряд несколько пробелов, то их следует заменить одним знаком "*", пробелы в начале и конце строки удалить'.split()
lst = '*'.join(string)
print(lst)