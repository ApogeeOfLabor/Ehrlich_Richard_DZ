# мне кажеться , что сделать задание именно через csv файл без прочитывания и перезаписи полностью, наверное не возможно.
# Если не править тупо ручками через Excel )) и то там наверное перезапись при сохранении.
# А бинарники явно не по уровню мне пока :)
def read_sales(argv):
    up_dict = dict()
    down_dict = dict()
    program, *args = argv
    if len(args) == 2:
        number, new_value = args
        with open('bakery.csv', 'r+', encoding='utf-8') as read_file:
            reader = csv.DictReader(read_file)
            for rows in reader:
                if rows['number'].isdigit() and int(rows['number']) < int(number):
                    up_dict[rows['number']] = rows['value']
                elif rows['number'].isdigit() and int(rows['number']) > int(number):
                    down_dict[rows['number']] = rows['value']
    return up_dict, down_dict


def modify_row_in_sale():
    show_sales.show_all_positions()
    number, new_value = input('Введите номер позиции для редактирования и новое значение через запятую без пробела: ').split(',')
    argv = './', number, new_value
    up_dict, down_dict = read_sales(argv)
    with open('bakery.csv', 'w+', encoding='utf-8') as file:
        file.seek(0)
        dict_for_write = {'number': 'some_name', 'value': 'some_name'}  # строчка для fieldnames, как оптимизировать лучше пока не знаю :)
        writer = csv.DictWriter(file, fieldnames=list(dict_for_write.keys()), quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerow(get_dict(up_dict))
        writer.writerow({'number': number, 'value': new_value})
        writer.writerow(get_dict(down_dict))


def get_dict(some_dict):
    for down_row in some_dict.items():
        return {'number': down_row[0], 'value': down_row[1]}


if __name__ == '__main__':
    import show_sales
    import csv
    exit(modify_row_in_sale())
