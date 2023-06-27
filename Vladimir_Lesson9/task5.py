class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title


    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)


    def draw(self):
        print('Пишем!')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)


    def draw(self):
        print('Рисуем!')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)


    def draw(self):
        print('Выдиляем!')


if __name__ == '__main__':
    h = Handle('Желтый маркер')
    h.draw()
    pc = Pencil('Карандаш')
    pc.draw()