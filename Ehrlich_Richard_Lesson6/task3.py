def get_passport_data(file_name):
    with open(file_name, 'r') as f:
        yield f.readlines()


def get_hobbies(file_name):
    with open(file_name, 'r') as f:
        yield f.readlines()


def make_file_with_dict_data(users_file, hobbies_file):
    user_data = list(get_passport_data(users_file))
    user_hobby = list(get_hobbies(hobbies_file))
    print(user_data, user_hobby)


if __name__ == '__main__':
    from make_file_library import make_files
    import os.path

    if not os.path.isfile('users.csv') and not os.path.isfile('hobby.csv'):
        make_files('users.csv', 'Иванов Иван Иванович\nПетров Петр Петрович\n')
        make_files('hobby.csv', 'скалолазание,охота\nгорные лыжи\n')
        print('DONE!')

    make_file_with_dict_data('users.csv', 'hobby.csv')
