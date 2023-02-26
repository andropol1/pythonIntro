# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def input_text():
    with open('file.txt', 'a') as data:
        data.write(input('Введите фамилию: '))
        data.write(' ')
        data.write(input('Введите имя: '))
        data.write(' ')
        data.write(input('Введите отчество: '))
        data.write(' ')
        data.write(input('Введите номер телефона: '))
        data.write('\n')


def print_text():
    data = open('file.txt', 'r')
    print()
    for line in data:
        print(line)
    data.close()


def check_text(user_info):
    data = open('file.txt', 'r')
    for line in data.readlines():
        if user_info in line:
            print(line)
    data.close()


def change_all_coincidence(old, new):
    with open('file.txt', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(old, new)

    with open('file.txt', 'w') as f:
        f.write(new_data)


def change_line(info):
    with open('file.txt') as data:
        list_add = []
        for line in data:
            if info in line.split():
                list_add.append(input('Введите новую строку: '))
            else:
                list_add.append(line)
    with open('file.txt', 'w') as data:
        data.writelines(list_add)


def delete_line(info):
    with open('file.txt') as data:
        list_del = []
        for line in data:
            if info in line:
                print(f'Данные по {line} удалены')
            else:
                list_del.append(line)
    with open('file.txt', 'w') as data:
        data.writelines(list_del)



match int(input('Если хотите добавить данные в телефонный справочник, введите 1; \n'
             'Если хотите вывести данные из телефонного справочника, введите 2; \n'
             'Если хотите произвести поиск по справочнику, введите 3; \n'
                'Если хотите заменить все совпадения по введеному тексту на новое, введите 4; \n'
                'Если хотите изменить конкретные данные, введите 5; \n'
                'Если хотите удалить строку, введите 6 ')):
    case 1:
        input_text()
    case 2:
        print_text()
    case 3:
        check_text(input('Введите данные '))
    case 4:
        change_all_coincidence(input('Введите текст, который хотите изменить '), input('Введите текст, на который хотите изменить '))
    case 5:
        change_line(input('Введите строку, который хотите изменить '))
    case 6:
        delete_line(input('Введите строку, которую хотите удалить'))

