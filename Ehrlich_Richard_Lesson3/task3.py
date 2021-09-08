def thesaurus(*args):
    names_database = dict()
    for _, name in enumerate(args):
        if name[0].upper() not in names_database.keys():
            names_database[name[0].upper()] = [name]
        else:
            names_database[name[0].upper()].append(name)
    return names_database


print(thesaurus("Петр", "Иван", "Мария", "Илья"))

