"""
*4. Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k,
сдвинув влево все элементы, стоящие правее элемента с индексом k.
- Программа получает на вход список (можно сгенерировать при помощи генератора случайных чисел), затем число k.
Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.
- Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя
использовать дополнительный список. Также не следует использовать метод pop(k) с параметром или оператор del.
"""
from random import randint

# random list with random range
my_list = [randint(1, 200) for i in range(randint(1, 20))]
print(my_list)
index = int(input("Input index number: "))
# cycle input index+1 to last index
for k in range(index+1, len(my_list)):
    # all elements from index+1 to last index, will be changed index - 1
    my_list[k-1] = my_list[k]
# last two elements will be same, need delete last one
my_list.pop()
print(my_list)