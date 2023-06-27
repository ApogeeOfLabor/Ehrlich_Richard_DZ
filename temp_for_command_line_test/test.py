from string import ascii_letters


class Person:
    __RUS = ''.join([chr(num) for num in range(1040, 1104)])

    def __init__(self, fio: str, old: int, doc: str, weight: float):
        self.__validation(fio)

        self.__fio = fio
        self.__old = old
        self.__doc = doc
        self.__weight = weight

    @classmethod
    def __validation(cls, fio: str):
        if not isinstance(fio, str) or len(fio.split()) != 3:
            raise TypeError('Не правельный тип данных! ФИО должно вводится в строку через пробел.')

        letters = ascii_letters + cls.__RUS
        for word in fio.split():
            if not len(word) or len(word.strip(letters)):
                raise TypeError('Не корректные сведения')


if __name__ == '__main__':
    pers = Person('Иванов Иван Иванович', 35, "1234 234235", 95.5)
