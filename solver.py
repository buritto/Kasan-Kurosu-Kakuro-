from cell_type import CellType
import copy
from kakuro_exxception import KakuroNotSolution


class Solver:

    def __init__(self, game):
        self.all_cells = []
        self.game = game
        self.solution = None

    def get_list(self):
        for x in range(0, self.game.height):
            for y in range(0, self.game.width):
                if self.game.field[x][y].get_type() == CellType.PLAY:
                    self.all_cells.append(self.game.field[x][y])

    def sort_solution(self, n, k):
        line = ""
        for cell in self.all_cells:
            line += str(cell.get_value())
        if self.is_correct_solve():
            self.solution = copy.deepcopy(self.game.field)
        if n == k:
            return
        for i in range(1, 10):
            self.all_cells[k].set_value(i)
            self.sort_solution(n, k + 1)

    def solve(self):
        self.get_list()
        self.sort_solution(len(self.all_cells), 0)
        if self.solution is None:
            raise KakuroNotSolution("Not solution")
        else:
            return self.solution

    def is_correct_solve(self):
        for pair in self.game.all_pairs:
            sum_row = 0
            sum_column = 0
            for pos_cell in pair.row_slaves:
                sum_row += self.game.field[pos_cell[0]][pos_cell[1]].get_value()
            for pos_cell in pair.column_slaves:
                sum_column += self.game.field[pos_cell[0]][pos_cell[1]].get_value()

            if sum_row != pair.cell.get_rules()[0] and pair.cell.get_rules()[0] != -1:
                    return False
            if sum_column != pair.cell.get_rules()[1] and pair.cell.get_rules()[1] != -1:
                return False
            expected_row = len(pair.row_slaves)
            expected_column = len(pair.column_slaves)
            actual_row = []
            actual_column = []
            for pos_cell in pair.row_slaves:
                actual_row.append(self.game.field[pos_cell[0]][pos_cell[1]].get_value())
            if len(set(actual_row)) != expected_row:
                return False
            for pos_cell in pair.column_slaves:
                actual_column.append(self.game.field[pos_cell[0]][pos_cell[1]].get_value())
            if len(set(actual_column)) != expected_column:
                return False
        return True
