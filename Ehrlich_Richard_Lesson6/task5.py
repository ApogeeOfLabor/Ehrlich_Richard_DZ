def makes_files(path, filename, text=None):
    filepath = os.path.join(path, filename)
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.isfile(filepath):
        with open(filepath, 'w') as file:
            if not text:
                text = str(input(f'Введите входные данные для файла {filepath}\nчерез запятую или введите None, если ввод данных не требуется: '))
                file.writelines(text.split(','))
            elif text:
                file.write(str(text))
            return True
    else:
        with open(filepath, 'a') as file:
            if not text:
                text = str(input(f'Вводите входные данные для файла {filepath}\nчерез запятую или введите None, если ввод данных не требуется: '))
                file.writelines(text.split(','))
            elif text:
                file.write(text)
            return True


def makes_binary_files(full_path_filename, text=None):
    if not os.path.isfile(full_path_filename):
        with open(full_path_filename, 'wb') as file:
            if text:
                file.write(text)
                # доработать запись бинарников
    else:
        with open(full_path_filename, 'ab') as file:
            if text:
                file.write(text)
                # доработать дозапись бинарников


def get_from_file_info(filename):
    with open(filename, 'r') as f:
        for string in f.readlines():
            yield string
            # дописать чтение и конвертацию бинарников


def get_from_binary_file_info(filename):
    with open(filename, 'rb') as f:
        for string in f.readlines():
            yield string


def make_file_with_dict_data(first_filename, second_filename):
    # корявый вывод данных в файл. Исправить.!
    # пересобрать или создать функцию работы с разными типами файлов
    user_data = [item.strip('\n,') for item in get_from_file_info(first_filename) if item]
    user_hobby = [item.strip('\n,') for item in get_from_file_info(second_filename) if item]
    dict_users_info = dict()
    for user_information, user_hobbies in zip([item if len(user_data) >= len(user_hobby) else sys.exit(1) for item in user_data],
                                              [user_hobby[index] if len(user_hobby) > index else None for index in range(len(user_data))]):
        dict_users_info[user_information] = user_hobbies
    return dict_users_info
    # допилить task4 потом продолжать


def check_extension(filename):
    return f"{filename.split('.')[-1]}"


def start():
    try:
        flag = False
        first_input_path, first_filename = input('Введите адрес первого файла: '), input('Введите имя первого файла first_filename.расширение: ')
        second_input_path, second_filename = input(f'Введите адрес второго файла: '), input(f'Введите имя второго файла second_filename.расширение: ')
        output_path, output_filename = input('Введите адрес файла с результатом работы скрипта: '), input('Введите имя файла с результатом работы скрипта output_filename.расширение: ')
        if first_input_path and first_filename and second_input_path and second_filename and output_path and output_filename:
            for file_name, file_path in zip([first_filename, second_filename], [first_input_path, second_input_path]):
                if check_extension(file_name) == 'bin' or check_extension(file_name) == 'pickle':
                    makes_binary_files(file_path, file_name)
                else:
                    flag = makes_files(file_path, file_name)
        else:
            print('Не корректный ввод данных!')
        if flag:
            output_dict = make_file_with_dict_data(os.path.join(first_input_path, first_filename), os.path.join(second_input_path, second_filename))
            makes_files(output_path, output_filename, text=output_dict)
        print('DONE!')
    except ValueError:
        print('Аргументы командной строки при запуске скрипта не предплагаются:\n'
              'Далее после запуска вам будет предложено ввести текст сначала для первого файла,\n'
              'далее для второго если он необходим, если нет просто введите None.\n')


if __name__ == '__main__':
    import sys
    import os.path
    # Можно сделать получение адресов и имён сразу из командной строки при старте скрипта,
    # но получаеться сильно длинная и не красивая строка
    exit(start())
