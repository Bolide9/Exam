import random
# Напишите программу: Дан список чисел. Определите, сколько в нем встречается различных чисел.
lst = list()

for i in range(1, 10):
    lst.append(random.randrange(1, 11))

print(len(set(lst)))
