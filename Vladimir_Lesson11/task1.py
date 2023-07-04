from datetime import date


class Date:
    __date = None

    def __init__(self, data: str):
        if len(data.split('-')) == 3:
            Date.__date = [int(num) for num in data.split('-')]
            Date.get_numbers()

    def __str__(self):
        if isinstance(self.__date, dict):
            return f'day: {self.__date["day"]}, month: {self.__date["month"]}, year: {self.__date["year"]}'

    @classmethod
    def get_numbers(cls):
        range_dict = {'day': (0, 31), 'month': (0, 12), 'year': (0, date.today().year)}
        if cls.check_range(cls.__date, range_dict):
            cls.__date = {key: int(value) for key, value in zip(range_dict.keys(), cls.__date)}

    @staticmethod
    def check_range(date_list: list, range_dict: dict):
        for key, (start, end) in zip(date_list, range_dict.values()):
            if not (start < key <= end):
                raise ValueError('Не правильный диапазон значений')
        return True


if __name__ == '__main__':
    cl = Date('1-5-2000')
    print(cl)
