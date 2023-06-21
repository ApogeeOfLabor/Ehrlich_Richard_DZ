class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, wage=0, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self) -> str:
        return f'{self.name} {self.surname}'

    def get_total_income(self) -> str:
        return f'{sum([num[1] for num in self._income.items()])}'


if __name__ == '__main__':

    position_ = Position('Vasya', 'Ivanov', 'master', 50000, 120000)

    print(f'name: {position_.name}', f'surname: {position_.surname}', f"position: {position_.position}", sep='\n')
    print(f"Full name: {position_.get_full_name()}, Income: {position_.get_total_income()}")
