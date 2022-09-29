"""
У вас есть список my_list с значениями типа int, и пустой список my_results.
Добавить в my_results те значения, которые больше 100.
Распечатать список my_results.
Задание выполнить с помощью цикла for.
"""
from random import randint

# random list with random range
my_list = [randint(1, 200) for i in range(randint(1, 20))]
print(my_list)
my_result = []
# cycle for elements in list which more than one hungered
for element in my_list:
    if element > 100:
        # elements more than one hungered appended to my_result
        my_result.append(element)
print(my_result)
