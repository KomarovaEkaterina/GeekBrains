from math import floor


class Cell:
    def __init__(self, num_of_cells):
        self.num_of_cells = num_of_cells

    # сложение
    def __add__(self, other):
        return Cell(self.num_of_cells + other.num_of_cells)

    # умножение
    def __mul__(self, other):
        return Cell(self.num_of_cells * other.num_of_cells)

    # вычитание
    def __sub__(self, other):
        n = ''
        tmp = self.num_of_cells - other.num_of_cells
        if tmp <= 0:
            n = -1
        else:
            n = tmp
        return Cell(n)

    # деление
    def __truediv__(self, other):
        n = ''
        tmp = floor(self.num_of_cells / other.num_of_cells)
        if tmp == 0:
            n = -1
        else:
            n = tmp
        return Cell(n)

    def __str__(self):
        tmp = ''
        if self.num_of_cells < 0:
            tmp = "Клетка расщипилась на молекулы!"
        else:
            tmp = self.num_of_cells * '*'
        return tmp

    def make_order(self, row):
        st = ''
        count_row = self.num_of_cells // row
        ost = self.num_of_cells % row
        for i in range(row):
            st += '*' * count_row + '\n'
        st += '*' * ost
        print(st)


cell_1 = Cell(3)
cell_2 = Cell(2)
print(f"{cell_1} + {cell_2} = {cell_1 + cell_2}")
print(f"{cell_1} - {cell_2} = {cell_1 - cell_2}")
print(f"{cell_2} - {cell_1} = {cell_2 - cell_1}")
print(f"{cell_1} * {cell_2} = {cell_1 * cell_2}")
print(f"{cell_1} / {cell_2} = {cell_1 / cell_2}")
print(f"{cell_2} / {cell_1} = {cell_2 / cell_1}")
print()
Cell(10).make_order(3)
