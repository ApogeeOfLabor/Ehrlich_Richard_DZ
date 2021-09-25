def makes_files(full_path_file_name, text=None):
    if not os.path.isfile(full_path_file_name):
        with open(full_path_file_name, 'w') as file:
            if text:
                file.write(text)
    else:
        with open(full_path_file_name, 'a') as file:
            if text:
                file.write(text)


def makes_binary_files(full_path_file_name, text=None):
    if not os.path.isfile(full_path_file_name):
        with open(full_path_file_name, 'wb') as file:
            if text:
                file.write(text)
                # доработать запись бинарников
    else:
        with open(full_path_file_name, 'ab') as file:
            if text:
                file.write(text)
                # доработать дозапись бинарников


def get_from_file_info(file_name):
    with open(file_name, 'r') as f:
        for string in f.readlines():
            yield string
            # дописать чтение и конвертацию бинарников


def get_from_binary_file_info(file_name):
    with open(file_name, 'rb') as f:
        for string in f.readlines():
            yield string


def make_file_with_dict_data(users_file, hobbies_file):

    # пересобрать или создать функцию работы с разными типами файлов
    user_data = [item.strip('\n,') for item in get_from_file_info('тут было название файла с прошлого задания') if item]
    user_hobby = [item.strip('\n,') for item in get_from_file_info('тут было название файла с прошлого задания') if item]

    dict_users_info = dict()

    for user_information, user_hobbies in zip([item if len(user_data) >= len(user_hobby) else sys.exit(1) for item in user_data],
                                              [user_hobby[index] if len(user_hobby) > index else None for index in range(len(user_data))]):
        dict_users_info[tuple(user_information.split())] = user_hobbies.split()

    return dict_users_info


if __name__ == '__main__':
    import sys
    import os.path

    # должна быть:
    # проверка на существование файлов с вопросом пересоздать или нет?
    if not os.path.isfile('users.csv') and not os.path.isfile('hobby.csv'):
        # make_files('hobby.csv', 'скалолазание, охота,\nгорные лыжи\n')
        # make_files('users.csv', 'Иванов Иван Иванович,\nПетров Петр Петрович\n')
        print('DONE!')

    print(make_file_with_dict_data('users.csv', 'hobby.csv'))
    # подаём путь и разные имена файлов с разным расширением для создания
    # реализовать дозапись информации в файлы из командной строки по необходимости

    exit('тут запускаеться главная функция с аргументами из командной строки sys.argv')