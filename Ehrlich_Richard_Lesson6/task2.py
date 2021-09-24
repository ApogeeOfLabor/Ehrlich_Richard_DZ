def get_spammer():
    with open('modify_log_nginx.txt', 'r') as file:
        log_list = [inner_string[1:-2].split() for inner_string in file.readlines()]
        # обрезаем круглые скобки и если я правильно понял в конце обрезается перевод коретки,
        # но почему-то он обрезается как один символ. Хотя визуально его вообще не было видно.
        for idx, inner_list in enumerate(log_list):
            for index, item_string in enumerate(inner_list):
                inner_list[index] = item_string.strip(" ,'")
            log_list[idx] = inner_list
        # чистка строк и списков для возможности работы с ними
        raw_dict = collections.Counter([get_ip[0] for get_ip in log_list])
        max_step_spammer = max(raw_dict.values())
        for key, value in raw_dict.items():
            if raw_dict[key] == max_step_spammer:
                return key, value


if __name__ == '__main__':
    import collections
    print(get_spammer())
