# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной
# и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
print('Введите количество монет')
n = int(input())
listOfCoins = []
count0 = 0
count1 = 0
for i in range(n):
    listOfCoins.append(int(input()))
    if listOfCoins[i] == 0:
        count0 += 1
    else:
        count1 += 1
if count0 <= count1:
    print(count0)
else:
    print(count1)
