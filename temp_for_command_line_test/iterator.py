class Iterator:

    """
    TODO: Разобраться и написать свой итератор
    """

    def __init__(self, start=0):
        self.index = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        ...


if __name__ == '__main__':

    x = [1, 2, 3, 54, 5, 6, 7, 8]