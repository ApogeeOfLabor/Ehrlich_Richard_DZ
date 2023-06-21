def add_sale(position_number, argv):
    program, income = argv
    dict_for_write = {'number': position_number, 'value': income}
    if os.stat('bakery.csv').st_size == 0:
        with open('bakery.csv', 'w+', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=list(dict_for_write.keys()), quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            writer.writerow(dict_for_write)
    else:
        with open('bakery.csv', 'a+', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=list(dict_for_write.keys()), quoting=csv.QUOTE_MINIMAL)
            writer.writerow(dict_for_write)


def read_db():
    if os.stat('bakery.csv').st_size == 0:
        return 1
    else:
        with open('bakery.csv', 'r+', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                position_number = int(row['number']) + 1
            return position_number


if __name__ == '__main__':
    import os
    import sys
    import csv
    exit(add_sale(read_db(), sys.argv))
