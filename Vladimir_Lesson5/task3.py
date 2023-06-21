def get_tuple_range(*args):
    tutors_, classes_ = args
    yield from zip(tutors_, (classes_[index] for index in range(len(tutors_))))


if __name__ == '__main__':
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
    classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

    print(*get_tuple_range(tutors, classes), sep='\n')
