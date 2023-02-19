# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
#
# Ввод:
# [-5,9,0,3,-1,-2,1,4,-2,1-,2,0,-9,8,10,-9,0,-5,-5,7]
# 5
# 15
# Вывод: [1,9,13,14,19]
import random

minimum, maximum = map(int, input('Введите минимум и максимум ').split())
listOfElements = [random.randint(-20, 20) for i in range(random.randint(4, 6))]
listOfIndex = [index for index, item in enumerate(listOfElements) if (minimum <= item <= maximum)]
print(listOfElements, listOfIndex, sep='\n')
