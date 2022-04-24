def get_passport_data(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def get_hobbies(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def make_file_with_dict_data(users_file, hobbies_file):

    user_data = [item.strip(',') for item in get_passport_data(users_file).split('\n') if item]
    user_hobby = [item.strip(',') for item in get_hobbies(hobbies_file).split('\n') if item]
    dict_users_info = dict()
    for user_information, user_hobbies in zip([item if len(user_data) >= len(user_hobby) else sys.exit(1) for item in user_data],
                                              [user_hobby[index] if len(user_hobby) > index else None for index in range(len(user_data))]):
        dict_users_info[user_information] = user_hobbies
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
