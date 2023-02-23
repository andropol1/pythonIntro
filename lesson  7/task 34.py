# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке |
# Ввод:
#
# пара-ра-рам рам-пам-папам па-ра-па-да
#
# Вывод:
# Парам пам-пам
text = 'пара-ра-рам рам-пам-папам па-ра-па-да'
vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = text.split()
if len(phrases) < 2:
    print('Количество фраз должно быть больше одной!')
else:
    countVowels = []
    for i in phrases:
        countVowels.append(len([j for j in i if j.lower() in vowels]))
    if countVowels.count(countVowels[0]) == len(countVowels):
        print('Парам пам-пам')
    else:
        print('Пам парам')
