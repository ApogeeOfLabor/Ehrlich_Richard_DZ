def num_translate(num):
    try:
        num_eng_ru = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'), \
                     ('один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')
        return f'{num_eng_ru[1][num_eng_ru[0].index(num)]}'
    except ValueError:
        return 'Введено неверное значение!'


print(num_translate(input('Input your number in english: ')))
