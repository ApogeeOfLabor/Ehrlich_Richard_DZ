# Проще пока что-то не вышло)

weather_report = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(weather_report), *weather_report)


def insert_quotation_mark(index_item, base_list):
    base_list.insert(index_item, '"')
    base_list.insert(index_item + 2, '"')
    return True


def get_string_from_list(modify_list):
    indexes = [i for i in weather_report if i[-1].isdigit()]
    for idx, child in enumerate(indexes):
        _tmp = ''.join(modify_list[modify_list.index(child) - 1:modify_list.index(child) + 2])
        modify_list.pop(modify_list.index(child) - 1)
        modify_list.pop(modify_list.index(child) + 1)
        modify_list[modify_list.index(child)] = _tmp
    return ' '.join(modify_list)


if __name__ == '__main__':
    list_of_found_numbers = [i for i in weather_report if i[-1].isdigit()]
    for item in list_of_found_numbers:
        insert_quotation_mark(weather_report.index(item), weather_report)
        weather_report[weather_report.index(item)] = '{0}{1:>02}'.format(weather_report[weather_report.index(item)][0], int(weather_report[weather_report.index(item)][-1])) if weather_report[weather_report.index(item)][0] == '+' else '{:>02}'.format(int(weather_report[weather_report.index(item)]))
    print(id(weather_report), weather_report)
    print(get_string_from_list(weather_report))
