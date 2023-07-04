class Cell:

    """ Работа с БИО клетками: сложение, деление, уножение и т.д. """

    __counter = 0

    def __init__(self, inner_cells):
        self.__inner_cells = inner_cells
        self.__counter += 1

    def __del__(self):
        self.__counter -= 1
        del self

    @property
    def inner_cells(self):
        return self.__inner_cells

    @inner_cells.setter
    def inner_cells(self, other: int):
        self.__inner_cells = other

    def __add__(self, other):
        if not isinstance(other, Cell):
            return 'Операция не возможна: На вход должен поступать экземпляр класса!'
        return self.inner_cells + other.inner_cells

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Операция не возможна: На вход должен поступать экземпляр класса!')
        if self.inner_cells - other.inner_cells > 0:
            return self.inner_cells - other.inner_cells
        else:
            return 'Операция не возможна: колличество ячеек в первой клетке должно превышать, колличество во второй!'

    def __mul__(self, other):
        if not isinstance(other, Cell):
            return 'Операция не возможна: На вход должен поступать экземпляр класса!'
        return self.inner_cells * other.inner_cells

    def __floordiv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Операция не возможна: На вход должен поступать экземпляр класса!')
        if self.inner_cells // other.inner_cells > 0:
            return self.inner_cells // other.inner_cells
        else:
            return 'Операция не возможна: колличество ячеек в первой клетке должно превышать колличество во второй, как минимум в два раза!'

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Операция не возможна: На вход должен поступать экземпляр класса!')
        if self.inner_cells / other.inner_cells >= 1:
            return int(self.inner_cells / other.inner_cells)
        else:
            return 'Операция не возможна: колличество ячеек в первой клетке должно превышать колличество во второй, как минимум в два раза!'

    def make_order(self, cells_in_row):
        if self.inner_cells >= cells_in_row:
            if self.inner_cells % cells_in_row:
                return '\n'.join(['*' * cells_in_row for _ in range(self.inner_cells // cells_in_row)] + ['*' * (self.inner_cells % cells_in_row)])
            return '\n'.join(['*' * cells_in_row for _ in range(self.inner_cells // cells_in_row)])
        else:
            return 'Операция не возможна: длина строки не должна превышать колличество ячеек в клетке!'


if __name__ == '__main__':

    a = Cell(5)
    b = Cell(12)

    c = Cell(a / b)
    print(c.inner_cells)

    print(b.make_order(7))

