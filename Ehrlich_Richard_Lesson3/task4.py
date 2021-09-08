

def thesaurus_adv(*args):
    humans_data = dict()
    for _, data in enumerate(args):
        if data[str(data).rindex(' ') + 1:][0] not in humans_data:
            humans_data[data[str(data).rindex(' ') + 1:][0]] = [data]
        else:
            humans_data[data[str(data).rindex(' ') + 1:][0]].append(data)
    print(humans_data)
    names_database = dict()
    for key, value in zip(humans_data.keys(), humans_data.values()):
        for index, name in enumerate(value):
            if name[:name.index(' ')][0] not in names_database.keys():
                if name[name.rindex(' ') + 1:][0] == key:
                    names_database[name[:name.index(' ')][0]] = [name]
            elif name[name.rindex(' ') + 1:][0] == key: # нужно смотреть не по key  а по фамилиям созданных словарей
                names_database[name[:name.index(' ')][0]].append(name)
        print(names_database)
    # Илья Иванов заходит не туда потому-что он видит что по ключу такой словарь создан и соответствует начальному key



print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
