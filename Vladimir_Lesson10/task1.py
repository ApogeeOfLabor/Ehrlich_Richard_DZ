import numpy as np


class Matrix:
    def __init__(self, seq):
        self.matrix = seq

    def __str__(self):
        new_matrix = ''
        for row in self.matrix:
            new_matrix += f'| {" ".join([f"{num}" for num in row])} |\n'
        return new_matrix

    def __add__(self, other: list):

        if set([len(item) for item in self.matrix]) != set([len(item) for item in other]):
            raise ValueError("Матрицы должны быть одной длинны")

        self.matrix = np.array(self.matrix) + np.array(other)
        return self

        # Самописный способ: сложение по индексам
        # for ind_l in range(len(self.matrix)):
        #     for ind_n in range(len(self.matrix[ind_l])):
        #         self.matrix[ind_l][ind_n] += other[ind_l][ind_n]
        # return self


if __name__ == '__main__':

    pt = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(pt)

    pt += [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(pt)
