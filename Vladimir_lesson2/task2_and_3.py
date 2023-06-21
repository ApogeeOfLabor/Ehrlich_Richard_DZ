def get_numbers(orig_list: list) -> list:
    return [item for item in orig_list if item[-1].isdigit()]


def insert_quotation_mark(index_item, base_list):
    base_list.insert(index_item, '"')
    base_list.insert(index_item + 2, '"')


def get_string_from_list(modify_list, numbers):
    for child in numbers:
        tmp_ = ''.join(modify_list[modify_list.index(child) - 1:modify_list.index(child) + 2])
        del modify_list[modify_list.index(child) - 1]
        del modify_list[modify_list.index(child) + 1]
        modify_list[modify_list.index(child)] = tmp_
    print(' '.join(modify_list))


def main():
    """ Можно сделать на регулярках быстрее и проще, но это будет выходить за рамки пройденого материала """
    weather_report = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

    orig_numbers = get_numbers(weather_report)
    mod_numbers = []
    for index, num in enumerate(orig_numbers):
        insert_quotation_mark(weather_report.index(num), weather_report)
        mod_numbers.append('{0}{1:>02}'.format(num[0], int(num[-1])) if num[0] == '+' else '{:>02}'.format(int(num)))
        weather_report[weather_report.index(num)] = mod_numbers[index]
    # print(id(weather_report), weather_report)
    get_string_from_list(weather_report, mod_numbers)


if __name__ == '__main__':
    main()


