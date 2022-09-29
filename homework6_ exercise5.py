"""
*5. Дан список целых чисел (можно сгенерировать при помощи генератора случайных чисел), число k и значение C.
Необходимо вставить в список на позицию с индексом k значение C, сдвинув все элементы, с индексом большим k, вправо.
Поскольку при этом количество элементов в списке увеличивается,
в конец списка нужно будет добавить новый элемент (любое значение), используя метод append().
- Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
- Использовать метод insert() не разрешается.
"""
from random import randint

# random list with random range
my_list = [randint(1, 200) for i in range(randint(1, 20))]
print(my_list)
index = int(input("Input index number: "))
element = input("Input element: ")
# need append one index, because list will be with one more elements
my_list.append(0)
# cycle from last index to input index with step minus one
for k in range(len(my_list) - 1, index, -1):
    # all elements from index to last index, will be changed index + 1
    my_list[k] = my_list[k - 1]
my_list[index] = element
print(my_list)
