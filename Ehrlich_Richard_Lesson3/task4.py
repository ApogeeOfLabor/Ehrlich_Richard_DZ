def thesaurus_adv(*args):
    key_by_lastname = dict()
    for _, data in enumerate(args):
        if data[data.rindex(' ') + 1:][0] not in key_by_lastname:
            key_by_lastname[data[data.rindex(' ') + 1:][0]] = [data]
        else:
            key_by_lastname[data[data.rindex(' ') + 1:][0]].append(data)

    key_by_name = dict()
    for key, value in key_by_lastname.items():
        for index, name in enumerate(value):
            if name[:name.index(' ')][0] not in key_by_name.keys():
                if name[name.rindex(' ') + 1:][0] == key:
                    key_by_name[name[:name.index(' ')][0]] = [name]
            elif name[name.rindex(' ') + 1:][0] == key:
                key_by_name[name[:name.index(' ')][0]].append(name)
        key_by_lastname[key] = {keys: values for keys, values in key_by_name.items()}
        key_by_name.clear()
    return key_by_lastname


if __name__ == '__main__':
    print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
