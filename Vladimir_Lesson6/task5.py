def get_from_file_info(filename):
    with open(filename, 'r') as f:
        for string in f.readlines():
            yield string


def make_dict(first_filename, second_filename):
    user_data = [item.strip('\n, ') for item in get_from_file_info(first_filename) if item]
    user_hobby = [item.strip('\n, ') for item in get_from_file_info(second_filename) if item]
    dict_users_info = dict()
    for user_information, user_hobbies in zip([item if len(user_data) >= len(user_hobby) else sys.exit(1) for item in user_data],
                                              [user_hobby[index] if len(user_hobby) > index else None for index in range(len(user_data))]):
        dict_users_info[user_information] = user_hobbies
    return dict_users_info


def start():
    try:
        print('Создаём файл с Ф.И.О пользователей: ')
        path_first_file = makes_files_with_dict_text()
        print('Создаём файл с хобби пользователей: ')
        path_second_file = makes_files_with_dict_text()

        print('Создаём результирующий файл: ')
        output_dict = make_dict(path_first_file, path_second_file)
        print(output_dict)
        makes_files_with_dict_text(text=output_dict)

        print('DONE!')
    except ValueError:
        print('Аргументы командной строки при запуске скрипта не предплагаются:\n'
              'Далее после запуска вам будет предложено ввести текст сначала для первого файла,\n'
              'далее для второго при необходимости, если нет просто введите None.\n')


if __name__ == '__main__':
    import sys
    from make_file_library import makes_files_with_dict_text
    # Можно сделать получение адресов и имён сразу из командной строки при старте скрипта,
    # но получаеться сильно длинная и не красивая строка
    exit(start())
