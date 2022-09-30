"""
Даны два списка чисел (можно сгенерировать при помощи генератора случайных чисел).
Посчитайте, сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.
- Примечание. Эту задачу можно решить в одну строчку.
"""
from random import randint

# random list1 with random range
my_list_1 = set([randint(1, 10) for i in range(randint(1, 10))] + [randint(1, 10) for k in range(randint(1, 10))])
print(my_list_1)
print(len(my_list_1))
