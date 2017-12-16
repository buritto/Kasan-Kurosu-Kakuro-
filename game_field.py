from game_cell import Cell
from cell_type import CellType


class GameField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.filed = []
        for x in range(0, height):
            self.filed[x] = []
            for y in range(0, width):
                self.filed[x][y] = Cell(CellType.NO_ACTIVE)

    def init_cell(self, x, y, cell):
        self.filed[x][y] = cell

    def check_correct_field(self):
        for x in range(0, self.height):
            for y in range(0, self.width):
                if self.filed[x][y].is_rules():
                    if not self.correct_row(x, y + 1, self.filed[x][y].get_length_row()):
                        return False
                    if not self.correct_column(x + 1, y, self.filed[x][y].get_length_column()):
                        return False
        return True

    def correct_row(self, pos_x, pos_y, length_row):
        for y in range(0, length_row):
            if self.filed[pos_x][pos_y + y].get_type() != CellType.PLAY:
                return False
        return True

    def correct_column(self, pos_x, pos_y, length_column):
        for x in range(0, length_column):
            if self.filed[pos_x + x][pos_y].get_type() != CellType.PLAY:
                return False
        return True


