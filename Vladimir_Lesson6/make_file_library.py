import os.path


def make_files(input_path='\n', filename=None, text=None):
    '''
    input_path='./', filename=None, text=None
    file.write(text)
    '''
    if not os.path.exists(input_path):
        os.makedirs(input_path)
    file_path = os.path.join(input_path, filename)
    with open(file_path, 'w') as file:
        if text:
            file.write(text)


def makes_files_with_dict_text(input_path='./', filename=None, text=None):
    ''' input_path='./', filename=None, text=None '''
    if not text:
        try:
            input_path = input('Тут вы можете указать адрес расположение файла или оставить поле пустым,\n'
                               'в таком случае файл будет сохранён в текущей дериктории\nВведите адрес: ')
            if input_path:
                if not os.path.exists(input_path):
                    os.makedirs(input_path)
        except FileNotFoundError:
            print('Введён не корректный адрес!')
        if not filename:
            if not check_extension(str(input_path)) == 'bin' or not check_extension(str(input_path)) == 'pickle':
                filename = input('Введите имя файла по шаблону"filename.расширение": ')
            else:
                print('Создание бинарных файлов не предусмотрено!')

        file_path = os.path.join(input_path, filename)
        with open(file_path, 'a', encoding='utf-8') as file:
            text = input(f'Введите входные данные для файла {filename}\nразделяя запятой '
                         f'или оставить поле пустым, если ввод данных не требуется: ')
            [file.writelines(item + '\n') for item in text.split(',')]
        return file_path
    else:
        try:
            input_path = input('Тут вы можете указать адрес расположение файла или оставить поле пустым,\n'
                               'в таком случае файл будет сохранён в текущей дериктории\nВведите адрес: ')
            if input_path:
                if not os.path.exists(input_path):
                    os.makedirs(input_path)
        except FileNotFoundError:
            print('Введён не корректный адрес!')
        if not filename:
            if not check_extension(str(input_path)) == 'bin' or not check_extension(str(input_path)) == 'pickle':
                filename = input('Введите имя файла по шаблону"filename.расширение": ')
            else:
                print('Создание бинарных файлов не предусмотрено!')

        file_path = os.path.join(input_path, filename)
        with open(file_path, 'a', encoding='utf-8') as file:
            [file.writelines(f'{item}\n') for item in text.items()]


def check_extension(filename):
    return f"{filename.split('.')[-1]}"


if __name__ == '__main__':
    make_files('users.csv', 'test text, again text')
