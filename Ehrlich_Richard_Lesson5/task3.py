def get_tuple_range():
    yield from zip(tutors, (klasses[index] if index < len(klasses) else None for index in range(len(tutors))))


if __name__ == '__main__':
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]

    print(type(get_tuple_range()), *get_tuple_range(), sep='\n')
