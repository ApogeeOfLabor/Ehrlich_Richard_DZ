def get_reader():
    with open('bakery.csv', 'r+', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for rows in reader:
            yield rows


def show_sale(argv):
    program, *args = argv
    if not args:
        for row in get_reader():
            if row['number'].isdigit():
                print(row['value'])
    elif len(args) == 1:
        for row in get_reader():
            if row['number'].isdigit() and int(row['number']) >= int(args[0]):
                print(row['value'])
    elif len(args) == 2:
        number_one, number_two = args
        for row in get_reader():
            if row['number'].isdigit() and int(number_one) <= int(row['number']) <= int(number_two):
                print(row['value'])


if __name__ == '__main__':
    import sys
    import csv
    exit(show_sale(sys.argv))
