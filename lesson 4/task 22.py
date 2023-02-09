# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
print('Введите кол-во элементов первого множества n')
n = int(input())
print('Введите кол-во элементов второго множества m')
m = int(input())
firstList = []
secondList = []
for i in range(n):
    firstList.append(int(input()))
for i in range(m):
    secondList.append(int(input()))
firstSet = set(firstList)
secondSet = set(secondList)
cross = sorted(firstSet.intersection(secondSet))
print(cross)
