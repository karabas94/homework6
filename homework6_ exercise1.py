"""
У вас есть список my_list с значениями типа int.
Распечатать те значения, которые больше 100.
Задание выполнить с помощью цикла for.
"""
from random import randint

# random list with random range
my_list = [randint(1, 200) for i in range(randint(1, 20))]
print(my_list)
# cycle for elements in list which more than one hungered
for element in my_list:
    if element > 100:
        # print elements which more than one hungered
        print(element, end=" ")
