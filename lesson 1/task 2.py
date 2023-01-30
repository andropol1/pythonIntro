# Задача 2: Найдите сумму цифр трехзначного числа.

print('Введите 3-х значное число')
value = int(input())
sumNumbers = value//100 + (value//10) % 10 + value % 10
print('Cумма цифр равна: ', sumNumbers)
