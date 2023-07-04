from abc import ABC, abstractmethod


class Clothes(ABC):
    """ Фабрика по производству костюмов и пальто"""
    __instance = None
    __x = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        self.__instance = None

    def __init__(self):
        super().__init__()
        self.__x.append(self)
        self.__type_name = 'Название продукции не задано!'

    @property
    def type(self) -> str:
        return self.__type_name

    @type.setter
    def type(self, type_name: str):
        if not any(item.lower() in ('костюм', 'пальто') for item in type_name.split()):
            raise TypeError('Разрешено создавать только "костюм" или "пальто"')
        self.__type_name = type_name

    def get_total_fabric_consumption(self):
        return sum([item.fabric_consumption for item in self.__x])

    @abstractmethod
    def fabric_consumption(self):
        ...


class Coat(Clothes):
    __counter = 0

    def __init__(self):
        super().__init__()
        self.__size = 'Размер ещё не задан!'
        self.__counter += 1

    def __del__(self):
        self.__counter -= 1
        del self

    @property
    def fabric_consumption(self):
        if not isinstance(self.__size, int):
            return f"Не возможно подсчитать расход {self.__size}"
        return self.__size / 6.5 + 0.5

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
        print(f'Первый экземпляр создан')


class Costume(Clothes):
    __counter = 0

    def __init__(self):
        super().__init__()
        self.__height = 'Рост ещё не задан!'
        self.__counter += 1

    def __del__(self):
        self.__counter -= 1
        del self

    @property
    def fabric_consumption(self):
        if not isinstance(self.__height, int):
            return f"Не возможно подсчитать расход {self.__height}"
        return 2 * self.__height + 0.3

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        print(f'Первый экземпляр создан')


if __name__ == '__main__':

    cs = Costume()
    co = Coat()

    cs.type = 'костюм'
    co.type = 'пальто'

    cs.height = 175
    co.size = 50

    print(cs)
    print(co)

    # Общий расход ткани можно узнать из любого экземпляра класса
    print(cs.get_total_fabric_consumption())
