from game_cell import Cell
from cell_type import CellType


class Pair:
    def __init__(self, cell):
        self.cell = cell
        self.slaves = []


class GameField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = []
        self.row_pairs = []
        self.column_pairs = []
        self.all_pairs = []
        for x in range(0, height):
            self.field.append([])
            for y in range(0, width):
                self.field[x].append(Cell(CellType.NO_ACTIVE))

    def init_cell(self, x, y, cell):
        self.field[x][y] = cell
        if cell.is_rules():
            pair = Pair(cell)
            self.all_pairs.append(pair)
            if cell.get_length_row():
                self.row_pairs.append(pair)
                self.init_row(x, y + 1, cell.get_length_row(), self.row_pairs[-1])
            if cell.get_length_column():
                self.column_pairs.append(pair)
                self.init_column(x + 1, y, cell.get_length_column(), self.column_pairs[-1])

    def check_correct_field(self):
        for x in range(0, self.height):
            for y in range(0, self.width):
                if self.field[x][y].is_rules():
                    if not self.correct_row(x, y + 1, self.field[x][y].get_length_row()):
                        return False
                    if not self.correct_column(x + 1, y, self.field[x][y].get_length_column()):
                        return False
        return True

    def correct_row(self, pos_x, pos_y, length_row):
        for y in range(0, length_row):
            if self.field[pos_x][pos_y + y].get_type() != CellType.PLAY:
                return False
        return True

    def correct_column(self, pos_x, pos_y, length_column):
        for x in range(0, length_column):
            if self.field[pos_x + x][pos_y].get_type() != CellType.PLAY:
                return False
        return True

    def init_row(self, pos_x, pos_y, length_row, pair):
        for y in range(0, length_row):
            cell = Cell(CellType.PLAY, 0)
            self.field[pos_x][pos_y + y] = cell
            pair.slaves.append(tuple([pos_x, pos_y + y]))

    def init_column(self, pos_x, pos_y, length_column, pair):
        for x in range(0, length_column):
            cell = Cell(CellType.PLAY)
            self.field[pos_x + x][pos_y] = cell
            pair.slaves.append(tuple([pos_x + x, pos_y]))
