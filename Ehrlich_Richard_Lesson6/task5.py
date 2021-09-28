def makes_files(filepath=None, text=None):
    if not text:
        flag = True
        while flag:
            try:
                input_path = input('Куда сохраняем файл?\nВведите адрес: ')
                filename = input('Введите имя файла по шаблону"filename.расширение": ')
                flag = False
            except FileNotFoundError:
                print('Введён не корректный адрес!')
        if check_extension(str(filepath)) == 'bin' or check_extension(str(filepath)) == 'pickle':
            print('Создание бинарных файлов не предусмотрено!')
        filepath = os.path.join(input_path, filename)
        if not os.path.exists(input_path):
            os.makedirs(input_path)
        # передумал докручивать навороты к условию задачи, много времени потерял.
        # Требования к задаче в методичке и на сайте разные, решил совместить.
        with open(filepath, 'a', encoding='utf-8') as file:
            if not text:
                text = str(input(f'Введите входные данные для файла {filename}\nразделяя запятой или введите None, если ввод данных не требуется: '))
                [file.writelines(item + '\n') for item in text.split(',')]
            elif text:
                file.write(text)
        return True, filepath
    else:
        try:
            input_path = input('Куда сохраняем файл?\nВведите адрес: ')
            filename = input('Введите имя файла по шаблону"filename.расширение": ')
            filepath = os.path.join(input_path, filename)
        except Exception:
            print('Не корректные данные!')
            sys.exit(1)
        with open(filepath, 'a', encoding='utf-8') as file:
            [file.writelines(f'{item}\n') for item in text.items()]


def get_from_file_info(filename):
    with open(filename, 'r') as f:
        for string in f.readlines():
            yield string


def make_file_with_dict_data(first_filename, second_filename):
    user_data = [item.strip('\n, ') for item in get_from_file_info(first_filename) if item]
    user_hobby = [item.strip('\n, ') for item in get_from_file_info(second_filename) if item]
    dict_users_info = dict()
    for user_information, user_hobbies in zip([item if len(user_data) >= len(user_hobby) else sys.exit(1) for item in user_data],
                                              [user_hobby[index] if len(user_hobby) > index else None for index in range(len(user_data))]):
        dict_users_info[user_information] = user_hobbies
    return dict_users_info


def check_extension(filename):
    return f"{filename.split('.')[-1]}"


def start():
    try:
        print('Создаём файл с Ф.И.О пользователей: ')
        path_first_file = makes_files()[-1]
        print('Создаём файл с хобби пользователей: ')
        path_second_file = makes_files()[-1]

        print('Создаём результирующий файл: ')
        output_dict = make_file_with_dict_data(path_first_file, path_second_file)
        print(output_dict)
        makes_files(text=output_dict)

        print('DONE!')
    except ValueError:
        print('Аргументы командной строки при запуске скрипта не предплагаются:\n'
              'Далее после запуска вам будет предложено ввести текст сначала для первого файла,\n'
              'далее для второго при необходимости, если нет просто введите None.\n')


if __name__ == '__main__':
    import sys
    import os.path
    # Можно сделать получение адресов и имён сразу из командной строки при старте скрипта,
    # но получаеться сильно длинная и не красивая строка
    exit(start())
