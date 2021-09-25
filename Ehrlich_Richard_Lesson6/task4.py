def get_passport_data(file_name):
    with open(file_name, 'r') as f:
        for string in f.readlines():
            yield string


def get_hobbies(file_name):
    with open(file_name, 'r') as f:
        for string in f.readlines():
            yield string


def make_file_with_dict_data(users_file, hobbies_file):

    user_data = [item.strip('\n,') for item in get_passport_data(users_file) if item]
    user_hobby = [item.strip('\n,') for item in get_hobbies(hobbies_file) if item]
    # Если объём данных будет больше ОЗУ, то вроде бы всё правильно сделал на генераторах
    # Если есть брешь в алгоритме, хотелось бы карающих развёрнутых комментариев)))

    dict_users_info = dict()
    # Думаю данное решение итераций с условиями внутри не самое элегантное, но иначе будет очень много if-ок
    for user_information, user_hobbies in zip([item if len(user_data) >= len(user_hobby) else sys.exit(1) for item in user_data],
                                              [user_hobby[index] if len(user_hobby) > index else None for index in range(len(user_data))]):
        dict_users_info[tuple(user_information.split())] = user_hobbies.split()
        # Как тут применить пункт парсинга понять особо не получается, если только так
        # как я сделал, преобразовав выходную строку в tuple, более ничего в голову пока не пришло.
        # Выбрал Tuple потому, что ключём может быть только immutable объект
        # а в значении проще чем лист мне кажеться не придумать :)
        # Одно значение разбито листом не логично типа ([горные, лыжи]) , но чтобы это реализовать, думаю без
        # специальных библиотек не обойтись. Каких именно, тоже пока не знаю. Явно попахивает Data Science.

    return dict_users_info


if __name__ == '__main__':
    from make_file_library import make_files
    import sys
    import os.path

    if not os.path.isfile('users.csv') and not os.path.isfile('hobby.csv'):
        make_files('hobby.csv', 'скалолазание, охота,\nгорные лыжи\n')
        make_files('users.csv', 'Иванов Иван Иванович,\nПетров Петр Петрович\n')
        print('DONE!')

    print(make_file_with_dict_data('users.csv', 'hobby.csv'))
    # Вывод: {('Иванов', 'Иван', 'Иванович'): ['скалолазание,', 'охота'], ('Петров', 'Петр', 'Петрович'): ['горные', 'лыжи']}
