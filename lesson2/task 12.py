# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

print('Введите сумму чисел S и произведение P')
S = int(input())
P = int(input())
flag = False
for i in range(1, 1000):
    for j in range(1, 1000):
        if i * j == P and (i + j) == S:
            x = i
            y = j
            flag = True
            break
    if flag:
        break
print(x, y)
