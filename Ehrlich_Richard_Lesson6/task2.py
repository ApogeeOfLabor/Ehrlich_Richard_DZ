def get_spammer():
    with open('modify_log_nginx.txt', 'r') as file:
        ip_counter = collections.defaultdict(int)
        for one_string in file.readlines():
            ip_counter[one_string[one_string.find("'")+1: one_string.index("'", one_string.find("'")+1)]] += 1
        max_step_spammer = max(ip_counter.values())
        for key, value in ip_counter.items():
            if ip_counter[key] == max_step_spammer:
                return key, value


if __name__ == '__main__':
    import collections
    print(get_spammer())
    # чувствую, что напрофессиональном уровне это всё на много проще и красивее выглядит,
    # но пока лучше не могу и то немного с твоей подсказкой:) - думаю в комитах это видно.
