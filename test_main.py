from game_field import GameField
from game_cell import Cell
from cell_type import CellType
from solver import Solver

all_list = []
i = 0
def bust_array(n, k):
    if (k == n):
        return
    for i in range(0, 9):
        all_list[k] = i
        print(all_list)
        bust_array(n, k + 1)



def print_field(field):
    for x in range(0, len(field)):
        line = ""
        for y in range(0, len(field)):
            if field[x][y].get_type() == CellType.NO_ACTIVE:
                line += ' # \t'
            if field[x][y].get_type() == CellType.PLAY:
                line += ' ' + str(field[x][y].get_value()) + ' \t'
            if field[x][y].get_type() == CellType.RULES:
                line += ' ' + str(field[x][y].get_rules()[1]) + '\\' + str(field[x][y].get_rules()[0]) + '\t'
        print(line)


if __name__ == '__main__':
    game = GameField(4, 4)
    #print_field(game.field)
    #print('===================================')
    game.init_cell(0, 1, Cell(CellType.RULES, column_rule=16, length_column=2))
    game.init_cell(0, 2, Cell(CellType.RULES, column_rule=15, length_column=3))
    game.init_cell(1, 0, Cell(CellType.RULES, row_rule=17, length_row=2))
    game.init_cell(2, 0, Cell(CellType.RULES, row_rule=15, length_row=3))
    game.init_cell(3, 1, Cell(CellType.RULES, row_rule=3, length_row=2))
    game.init_cell(1, 3, Cell(CellType.RULES, column_rule=4, length_column=2))
    print_field(game.field)
    solver = Solver(game)
    new_field = solver.solve()
    print_field(new_field)






