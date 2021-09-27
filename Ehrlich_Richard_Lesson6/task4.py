def get_passport_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for string in f.readlines():
            yield string


def get_hobbies(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for string in f.readlines():
            yield string


def make_file_with_dict_data(users_file, hobbies_file):
    users_data = (item.strip('\n,') for item in get_passport_data(users_file) if item)
    users_hobby = (item.strip('\n,') for item in get_hobbies(hobbies_file) if item)

    dict_users_info = dict()
    # пока запутался как реализовать условие с выдачей None на генераторах
    for user_information, user_hobbies in zip(users_data, users_hobby):
        if user_information and user_hobbies:
            dict_users_info[user_information] = user_hobbies
        elif user_information and not user_hobbies:
            dict_users_info[user_information] = None
        elif user_hobbies and not user_information:
            sys.exit(1)

    return dict_users_info


def make_final_file():
    pass


if __name__ == '__main__':
    from make_file_library import make_files
    import sys
    import os.path

    #if not os.path.isfile('users.csv') and not os.path.isfile('hobby.csv'):
    make_files('hobby.csv', 'скалолазание, охота,\nгорные лыжи\n')
    make_files('users.csv', 'Иванов Иван Иванович,\nПетров Петр Петрович\nПетров Петр Петрович\nПетров Петр Петрович\n')
    print('DONE!')

    print(make_file_with_dict_data('users.csv', 'hobby.csv'))
