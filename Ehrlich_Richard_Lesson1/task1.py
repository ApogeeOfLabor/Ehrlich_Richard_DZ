unit = (
    ('day', 86400),
    ('hour', 3600),
    ('minute', 60),
    ('second', 1)
)


def get_time_distance(unit_list, seconds):
    time_dict = {}
    for unit_name, sec in unit_list:
        units = seconds // sec
        time_dict[unit_name] = units
        if units:
            seconds -= units * sec
        else:
            continue
    result = ("{} д ".format(time_dict['day']) if time_dict['day'] else '') + \
             ("{} час ".format(time_dict['hour']) if time_dict['hour'] else '') + \
             ("{} мин ".format(time_dict['minute']) if time_dict['minute'] else '') + \
             ("{} сек ".format(time_dict['second']) if time_dict['second'] else '')
    return result


if __name__ == '__main__':
    user_sec = int(input('Введите колличество секунд: '))
    print(get_time_distance(unit, user_sec))
