def get_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for string in f.readlines():
            yield string


def make_file(users_file, hobbies_file):
    users_data = (item.strip('\n,') for item in get_data(users_file) if item)
    users_hobby = (item.strip('\n,') for item in get_data(hobbies_file) if item)
    for user_information, user_hobbies in zip_longest(users_data, users_hobby):
        if not user_information:
            print('Ошибка данных!')
            sys.exit(1)
        with open('users_hobby_for_task4.txt', 'a', encoding='utf-8') as f:
            f.writelines(f'{user_information}: {user_hobbies}\n')
            # Вывод в консоль:
            # Иванов Иван Иванович: скалолазание, охота
            # Петров Петр Петрович: горные лыжи


if __name__ == '__main__':
    from make_file_library import make_files
    from itertools import zip_longest
    import os.path
    import sys

    if not os.path.isfile('users.csv') and not os.path.isfile('hobby.csv'):
        make_files('./', 'hobby.csv', 'скалолазание, охота,\nгорные лыжи,\nгорные лыжи')
        make_files('./', 'users.csv', 'Иванов Иван Иванович,\nПетров Петр Петрович')
        print('DONE!')

    make_file('users.csv', 'hobby.csv')
