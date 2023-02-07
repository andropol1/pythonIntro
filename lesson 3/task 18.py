# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai . Последняя строка содержит число X
print('Введите число N')
N = int(input())
print('Введите число X')
X = int(input())
A = []
for i in range(N):
    A.append(int(input()))
dif = abs(X - A[0])
closerOne = A[0]
for i in range(N):
    if abs(X - A[i]) < dif:
        dif = abs(X - A[i])
        closerOne = A[i]
print(closerOne)
