import collections

"""
Напишите программу, которая принимает текст и выводит три слова: наиболее часто встречающееся, самое длинное и самое короткое
"""

# Задаем условный текст
text = '''
Невод рыбак расстилал по брегу студеного моря;
Мальчик отцу помогал. Отрок, оставь рыбака!
Мрежи иные тебя ожидают, иные заботы:
Будешь умы уловлять, будешь помощник царям.
'''

# Разбиваем текст по одному слову
sp_text = text.split()


# Объявляем функцию, которая возвращает три слова: наиболее часто встречающееся, самое длинное и самое короткое
def counting(_sp_text):
    # Часто встречающееся
    most_common = collections.Counter(_sp_text).most_common()
    print(most_common[0])

    # Самое длинное
    most_len = max(_sp_text, key=len)
    print(most_len)

    # Самое короткое
    most_short = min(_sp_text, key=len)
    print(most_short)


counting(sp_text)