def num_translate(num):
    try:
        num_eng_ru = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'), \
                     ('один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')
        # просто для читаемости кода получил индекс отдельной строкой
        _index = num_eng_ru[0].index(num.lower())
        return '{}'.format(num_eng_ru[1][_index]) if num.islower() else '{}'.format(num_eng_ru[1][_index].capitalize())
    except ValueError:
        return 'Введено неверное значение!'


print(num_translate(input('Input your number in english: ')))
