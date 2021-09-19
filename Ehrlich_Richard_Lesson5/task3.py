def get_tuple_range():
    if len(tutors) <= len(klasses):
        yield from zip(tutors, klasses)
    else:
        # Понятно что костыль, но по другому прям что-то никак не мог придумать
        [klasses.append(None) for _ in range(len(tutors) - len(klasses))]
        yield from zip(tutors, klasses)


if __name__ == '__main__':
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]

    print(type(get_tuple_range()), *get_tuple_range(), sep='\n')
