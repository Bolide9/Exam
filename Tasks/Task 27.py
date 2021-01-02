'''
Напишите программу, которая на вход принимает строку, необходимо вывести 2 списка, первый содержит слова, второй числа.
'''
import re

string = input()

nums = re.findall(r'\d+', string)
nums = [i for i in nums if i.isdigit()]

letters = re.findall(r'[a-zA-Zа-яА-Я]', string)
letters = [i for i in letters if i.isalpha()]

print(nums)
print(letters)

# если необходимо вывести то слова выводятся примерно так:
# print(''.join(map(str, letters)))
