from cell_type import CellType
from game_cell import Cell
from game_field import GameField


class Colver:

    def __init__(self, game_field):
        self.gameField = game_field

    def solve(self, field):
        if not self.field_is_empty(field):
            return field
        else:
            previous_field = field.copy()
            position = self.get_position(field)
            values = self.get_values(position[0], position [1], field)
            for value in values:
                pos_x = position[0]
                pos_y = position[1]
                field[pos_x, pos_y].set_value(value)
            field = previous_field

    def field_is_empty(self, field):
        for x in range(0, field.height):
            for y in range(0, field.width):
                if field[x][y].get_type() == CellType.PLAY and field[x][y].get_value() == 0:
                    return True
        return False

    def get_position(self, field):
        for x in range(0, field.height):
            for y in range(0, field.width):
                if field[x][y].get_type() == CellType.PLAY and field[x][y].get_value() == 0:
                    return [x, y]
        raise Exception()

    def get_values(self, x, y, field):
        cell = field[x, y]
        value_row = []
        value_column = []
        for pair in field.row_pairs():
            if cell in pair.slaves:
                value = 0
                for slave in pair.slaves:
                    value = value + slave.get_value()
                value_row = [i for i in range(0, 9) if pair.cell.get_rules()[0] - value - i > 0]

        for pair in field.column_pairs():
            if cell in pair.slaves:
                value = 0
                for slave in pair.slaves:
                    value = value + slave.get_value()
                value_row = [i for i in range(0, 9) if pair.cell.get_rules()[1] - value - i > 0]
        return set(value_row + value_column)
