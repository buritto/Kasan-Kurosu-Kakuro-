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

    def bust_array(self, n, k):
        if self.is_correct_solve():
            self.solution = copy.deepcopy(self.game.field)
        if n == k:
            return
        for i in range(1, 10):
            self.all_cells[k].set_value(i)
            self.bust_array(n, k + 1)

    def solve(self):
        self.get_list()
        self.bust_array(len(self.all_cells), 0)
        if self.solution is None:
            raise KakuroNotSolution("Not solution")
        else:
            return self.solution

    def is_correct_solve(self):
        for pair in self.game.all_pairs:
            sum = 0
            for pos_cell in pair.slaves:
                sum += self.game.field[pos_cell[0]][pos_cell[1]].get_value()
            if sum != pair.cell.get_rules()[0] and sum != pair.cell.get_rules()[1]:
                return False
            expected = len(pair.slaves)
            actual = []
            for pos_cell in pair.slaves:
                actual.append(self.game.field[pos_cell[0]][pos_cell[1]].get_value())
            if len(set(actual)) != expected:
                return False
        return True
